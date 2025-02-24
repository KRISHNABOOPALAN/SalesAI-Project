from django.shortcuts import render,redirect

# Create your views here.

def HOME(request):
    return render(request,'Home.html')