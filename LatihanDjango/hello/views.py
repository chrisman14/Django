from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	#return HttpResponse('<h1>coba</h1>')
	name=request.GET.get('name','word')
	gree=request.GET.get('gree','word')
	# name=request.GET['name']
	return render(request, 'hello/index.html',{'greetings':gree,'name':name})