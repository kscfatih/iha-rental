from django.shortcuts import render, redirect
from django.http import HttpResponse
from management.models import Kategori
from datetime import datetime

def index(request):
    kategori = Kategori.objects.all()
    now = datetime.now().strftime("%Y-%m-%dT%H:%M")
    return render(request,"panel/IHA/hire.html",{'kategoriler':kategori,'now': now})

def rented_iha(request):
    kategori = Kategori.objects.all()
    return  render(request,"panel/IHA/rented-iha.html",{'kategoriler':kategori})
