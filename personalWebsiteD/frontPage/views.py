from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "frontPage/index.html")

def collin(request):
    return HttpResponse("Cfitz")

def greet(request, name):
    return render(request, "frontPage/greet.html", {
        "name": name.capitalize()
    })