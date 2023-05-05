from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
import stripe
from django.urls import reverse
from datetime import datetime,timedelta

# Create your views here.
def index(request):
    return render(request, 'index.html')
