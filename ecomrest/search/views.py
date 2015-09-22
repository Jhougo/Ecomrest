# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Vehicale, People
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import PeopleSerializer, VehicaleSerializer

@csrf_exempt
def vehicale_list(request):
    if request.method == 'GET':
        vehicale = Vehicale.objects.all()
        serializer = VehicaleSerializer(vehicale, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehicaleSerializer(data=data)
        serializer.save()
        return JSONResponse(serializer.data, status=201)

def vehicale_detail(request, pk):
    try:
        vehicale = Vehicale.objects.get(plate=pk)
    except Vehicale.DoesNotExist:
        return HttpResponse(print(pk))

    if request.method =='GET':
        serializer = VehicaleSerializer(vehicale)
        return JSONResponse(serializer.data)
    elif request.method == 'put':
        data = JSONParser().parse(request)
        serializer = VehicaleSerializer(vehicale, data=data)
        serializer.save()
        return (serializer.data)

def people_list(request):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JSONResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeopleSerializer(data=data)
        serializer.save()
        return JSONResponse(serializer.data, status=201)

def people_detail(request, pk):
    try:
        people = People.objects.get(people_id=pk)
    except People.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return JSONResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeopleSerializer(people, data=data)
        serializer.save()
        return JSONResponse(serializer.data)

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

