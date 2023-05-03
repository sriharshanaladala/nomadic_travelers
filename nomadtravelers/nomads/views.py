from django.shortcuts import render
from django.http import HttpResponse


def nomads(request):
    msg="hello you are in the project page"
    return render(request,'nomads/nomads.html',{'msg':msg})


def nomad(request,pk):
    return render(request,'nomads/nomad.html')
