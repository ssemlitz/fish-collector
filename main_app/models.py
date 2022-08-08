from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Fish(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('fishies_detail', kwargs={'fish_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
    )

  fish = models.ForeignKey(Fish, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']
  

