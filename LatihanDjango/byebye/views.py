from django.shortcuts import render
from django.http import HttpResponse


def coba(request):
	return HttpResponse('<h1>bye - bye</h1>')
