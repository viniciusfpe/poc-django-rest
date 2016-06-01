# -*- coding: utf-8 -*-
from django.db import models

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=80)
    create_user = models.CharField(max_length=20)
    create_date = models.DateTimeField()