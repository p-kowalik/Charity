document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }



    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;
      if (this.currentStep === 3){
        displayValidInstitutions()

      }
      if (this.currentStep === 5){
        passFormValues();
      }

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});



/*generate list of donation categories selected*/
var category_list = [];
function addValueToCategoryList(event) {
  category_list = [];
  var checkboxes = document.getElementsByName("categories");
  for (var i=0; i<checkboxes.length; i++) {
    var checkbox = checkboxes[i];
    if (checkbox.checked) {
      category_list.push(checkbox.dataset.id)
    }
  }
}

/*display institutions accepting selected categories of donations*/
function displayValidInstitutions() {
  var institutions = document.getElementsByName("organization");
  var institution_form = document.querySelectorAll(".form-group.form-group--checkbox.step3");
  for (var i=0; i<institutions.length; i++) {
    for (var k = 0; k < institution_form.length; k++) {
      var form_item = institution_form[k];
      form_item.classList.add("form-no-display");
    }
  }
  for (var s=0; s<institutions.length; s++) {
    var institution = institution_form[s];
    var institution_categories = institution.querySelector("input").dataset.categoryIds.split(',');
    for (var j=0; j<category_list.length; j++) {
      var category_list_object = category_list[j];
      if (institution_categories.includes(category_list_object)) {
        institution.classList.remove("form-no-display")
      }
    }
  }
}

/*pass values from form inputs to summary sheet*/
function passFormValues() {
  /*summary of bags to be donated (add categories description)*/
  var bags_amount = document.getElementById("bags").value;
  document.getElementById("list_bags_amount").innerHTML = bags_amount;

  /*summary of foundation*/
  var institutions = document.getElementsByName("organization");
  for (var i=0; i<institutions.length; i++) {
    if (institutions[i].checked) {
      var institution_name = institutions[i].dataset.instname;
      document.getElementById("institution_name_summary").innerHTML = institution_name;
    }
  }

  /*summary of delivery address*/
  var delivery_address_tag = document.getElementById("address");
  var delivery_address_inputs = delivery_address_tag.getElementsByTagName('input');
  var delivery_address_summary_tag = document.getElementById("address_summary");
  var delivery_address_summary_list_element = delivery_address_summary_tag.getElementsByTagName('li');
  for (var h=0; h<delivery_address_inputs.length; h++) {
    delivery_address_summary_list_element[h].innerHTML = delivery_address_inputs[h].value;
  }

  /*summary of delivery date and comment for courier*/
  var reception_date_tag = document.getElementById("reception_date_input");
  var reception_date_inputs = reception_date_tag.getElementsByTagName('input');
  var reception_date_summary_tag = document.getElementById("reception_date_summary");
  var reception_date_summary_list_element = reception_date_summary_tag.getElementsByTagName('li');
  for (var g=0; g<reception_date_inputs.length; g++) {
    reception_date_summary_list_element[g].innerHTML = reception_date_inputs[g].value;
  }
  var delivery_comment = document.getElementById("more_info");
  document.getElementById("delivery_comment_summary").innerHTML = delivery_comment.value;
}
