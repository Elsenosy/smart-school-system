from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
# Create your views here.

def index(request):
    timenow = timezone.now().date()
    return HttpResponse(timenow)