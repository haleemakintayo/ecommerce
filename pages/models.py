from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    product_image = models.ImageField(upload_to='products/')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_desc = models.TextField(max_length=2040)

    def __str__(self):
        return self.product_name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    datetime = models.DateTimeField()
    # Assuming you have a predefined set of choices for the number of people
    NO_OF_PEOPLE_CHOICES = [
        (1, 'People 1'),
        (2, 'People 2'),
        (3, 'People 3'),
        (4, 'People 4'),
    ]
    no_of_people = models.IntegerField(choices=NO_OF_PEOPLE_CHOICES)
    special_request = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.datetime}"
