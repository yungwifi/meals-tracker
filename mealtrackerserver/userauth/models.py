# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
                             
from mealtrackerserver import helper
                                                   
class User(AbstractUser):
    hash_id = models.CharField(max_length=32, default=helper.create_hash, unique=True)
