from __future__ import unicode_literals
from datetime import timedelta
from django.db import models



class Meal(models.Model):
    meal_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    cook_time = models.DurationField(default=timedelta(minutes=40))
    prep_time = models.DurationField(default=timedelta(minutes=10))
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.meal_name

    class Meta:
        ordering = ('pub_date',)


class Ingredient(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        ordering = ('ingredient_name',)
