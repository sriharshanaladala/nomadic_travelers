from django.shortcuts import render
from django.http import HttpResponse

def nomads(request):
    return HttpResponse('here we can se our nomads')
def nomad(request,pk):
    return HttpResponse("single user"+''+ str(pk))