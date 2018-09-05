# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Meal, Ingredient

# Register your models here.
admin.site.register(Meal)
admin.site.register(Ingredient)
