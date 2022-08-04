from django.http import HttpResponse
from django.shortcuts import render
from . models import book

# Create your views here.
def demo(request):
   obj=book.objects.all()
   return render(request,'index.html',{'result':obj})

