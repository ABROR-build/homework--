from django.shortcuts import render
from django.http import HttpResponse


def customers_list(request):
    return HttpResponse('<h1>What do you want to buy</h1>')
