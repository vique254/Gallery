from django.shortcuts import render
from django.http  import HttpResponse
# Create your views her
def welcome(request):
    return HttpResponse('Welcome to Gall')
    return HttpResponse(html)