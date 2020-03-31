










  var CategoryList = [];
  function addValueToCategoryList(checkbox) {
      if(checkbox.checked == true){
        var Category = document.getElementsByName("categories");
        var CategoryValue = Category.value();
        CategoryList.push(CategoryValue);
        console.log(CategoryList);





var CategoryList = [];
function addValueToCategoryList(checkbox) {
    if(checkbox.checked == true){
      var Category = document.getElementsByName("categories");
      var CategoryValue = Category.value;
      CategoryList.push(CategoryValue);
      console.log(CategoryList);

var InstitutionsMatchingList = [];
var institutions = document.getElementsByName("organization");


function displaySelectedIfHidden(checkbox) {
    if(checkbox.checked == true){
        document.getElementById("submit").removeAttribute("disabled");
    }else{
        document.getElementById("submit").setAttribute("disabled", "disabled");
   }
}


    var categories_all = document.getElementsByName("categories");
    categories_all.forEach(classList.toggle("form-no-display"));
        (displaySelectedIfHidden);
    function displaySelectedIfHidden(value) {classList.toggle("form-no-display")};

    var categories_checked = document.getElementsByName("categories");
    console.log(categories_checked)
for (var i = 0; i < categories_checked.length; i++) {
if (check_box.firstElementChild.checked === true);

}
    var institution_matching = document.getElementsByName("organization");



    if (this.checked === true) {
            invoice_field.className = "form-group";
        } else {
            invoice_field.className = "hidden"
        }
    var donation_types = document
    var donation_types_selected =
    institution_matching.addEventListener("change", function () {
        var invoice_field = document.getElementById("invoiceData");
        if (this.checked === true) {
            invoice_field.className = "form-group";
        } else {
            invoice_field.className = "hidden"
        }
    });


    var check_box = document.getElementsByName("categories");
    check_box.addEventListener("change", function () {
        var invoice_field = document.getElementById("invoiceData");
        if (this.checked === true) {
            invoice_field.className = "form-group";
            invoice_field.dataset.checked = "1"
        } else {
            invoice_field.className = "hidden"
            invoice_field.dataset.checked = "0"
        }
    })
