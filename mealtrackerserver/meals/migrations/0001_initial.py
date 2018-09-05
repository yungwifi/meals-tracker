# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 17:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('cook_time', models.DurationField(default=datetime.timedelta(0, 2400))),
                ('prep_time', models.DurationField(default=datetime.timedelta(0, 600))),
                ('vegeterian', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal'),
        ),
    ]
