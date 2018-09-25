from rest_framework import serializers
from meals.models import Meal, Ingredient


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Meal
        fields = ('meal_name', 'pub_date', 'cook_time', 'prep_time', 'vegetarian')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Ingredient 
        fields = ('meal', 'ingredient_name')