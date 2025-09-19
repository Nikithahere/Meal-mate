from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default="https://static.vecteezy.com/system/resources/previews/052/792/818/non_2x/restaurant-logo-design-vector.jpg")
    cuisine = models.CharField(max_length = 200)
    rating = models.FloatField()

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.URLField(default="https://example.com/default.jpg")



    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"
    # dummy change

