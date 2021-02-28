from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import uygulama

# Create your views here.

def Uygulama_index(request):
    Uygulamas=uygulama.objects.all()
    return render(request,'Uygulama/index.html',{'Uygulamas':Uygulamas})
def Uygulama_detail(request):
    Uygulama=uygulama.objects.get(id=1)
    return HttpResponse('www.bursbasvuru.com')
def Uygulama_create(request):
    return HttpResponse('Burası Uygulama create sayfası')
def Uygulama_update(request):
    return HttpResponse('Burası Uygulama update sayfası')
def Uygulama_delete(request):
    return HttpResponse('Burası Uygulama delete sayfası')


