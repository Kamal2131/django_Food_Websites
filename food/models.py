from django.db import models

# Create your models here.
class food(models.Model):
    food_name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=100)
    food_price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.food_name
