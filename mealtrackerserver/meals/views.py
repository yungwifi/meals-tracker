# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from meals.models import Meal
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from meals.serializers import MealSerializer


def index(request):

    if request.method == 'GET':
        meal_list = Meal.objects.all()
        serializer = MealSerializer(meal_list, many=True)
        return JsonResponse(serializer.data, safe=False)


def show(request, id):

    if request.method == 'GET':
        meal = Meal.objects.get(id=id)
        serializer = MealSerializer(meal, many=True)
        return JsonResponse(serializer.data, safe=False)
