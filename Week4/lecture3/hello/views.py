from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def bomba(request):
    return HttpResponse("Walaszek grubasie kiedy nowy...")
 
def greet(request, name):
    name = name.capitalize()
    return render(request, "hello/greet.html", {
        "name": name
        })