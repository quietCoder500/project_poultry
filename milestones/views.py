from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request, project_slug):
    return HttpResponse("Hello, world! This is a response.")
