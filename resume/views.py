from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def index(request):
    
    return render(request, 'home1.html')