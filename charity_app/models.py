from django.db import models
from django.contrib.auth.models import User
from django.core.validators import EmailValidator, URLValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name




TYPES = (
    (1, 'fundacja'),
    (2, 'organizacja pozarządowa'),
    (3, 'zbiórka lokalna')
)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.IntegerField(choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    @property
    def category_ids(self):
        return ','.join([str(category.id) for category in self.categories.all()])


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str("Podarunek dla : ") + str(self.institution) + str(", z dnia : ") + str(self.pick_up_date)
