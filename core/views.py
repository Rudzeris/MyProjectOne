from django.http import HttpResponse
from django.shortcuts import render


def Hi(request):
    return HttpResponse('Hi')