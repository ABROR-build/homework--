from django.shortcuts import render
from django.http import HttpResponse


def sellers_list(request):
    return HttpResponse('<h1>What do you want to sell</h1>')
