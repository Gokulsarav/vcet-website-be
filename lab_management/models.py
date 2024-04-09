# lab_management/models.py

from django.db import models

class LabData(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    component = models.CharField(max_length=100)
    manufacturer_year = models.CharField(max_length=10)
    bought_year = models.CharField(max_length=10)
    working_condition = models.CharField(max_length=20)
