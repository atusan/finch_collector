from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
    ('C', 'Cleaning'),
    ('D', 'Dusting'),
    ('F', 'Fixing')
)
# Create your models here.

class Location(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address


class Art(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('detail', kwargs={'art_id': self.id})

class Feeding(models.Model):
        date = models.DateField()
        meal = models.CharField(
            max_length=1,
            choices=MEALS,
            default=MEALS[0][0]
        )
        # Create a cat_id FK
        art = models.ForeignKey(Art, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.get_meal_display()} on {self.date}"

