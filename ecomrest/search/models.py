# -*- coding: utf-8 -*-
from django.db import models

# Vehical's variable which we want to get from database
class Vehicale(models.Model):
    #How many time  this plate violate
    ve_vio_count = models.CharField(max_length=255)
    #Vehicale late number
    plate = models.CharField(max_length=20, primary_key=True)
    #Date of violate happend
    vio_date = models.CharField(max_length=20)
    #When violate happend(exact time)
    vio_time = models.CharField(max_length=20)
    vehicale_type = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    vehicale_brand = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    type_detail = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#People who violate
class People(models.Model):
    #How many time this people violate
    peo_vio_count = models.CharField(max_length=255)
    #People's id
    people_id = models.CharField(max_length=50, primary_key=True)
    #people' name
    name = models.CharField(max_length=255)
    #people's address
    address =models.CharField(max_length=255)
    #date of violate happend
    peo_vio_date = models.CharField(max_length=255)
    #When violate happend(exact time)
    peo_vio_time = models.CharField(max_length=255)


    def __str__(self):
        return self.name
