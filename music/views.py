from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
     return HttpResponse("<h2> Checking .... .........!! </h2>")


def details(request, album_id):
    return HttpResponse("<h4> Album No : "+album_id+"</h4>")
