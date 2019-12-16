from django.shortcuts import render
from .models import Image,location,category
from django.http  import HttpResponse
# Create your views her
def welcome(request):
    return render(request,'index.html')
    