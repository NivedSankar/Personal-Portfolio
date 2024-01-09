
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# from .forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')
