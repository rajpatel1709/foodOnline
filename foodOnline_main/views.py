from django.shortcuts import render
from django.http import HttpResponse
#this file is just module
#function for home page
def home(request):
    return HttpResponse("hello my world")