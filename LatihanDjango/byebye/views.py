from django.shortcuts import render
from django.http import HttpResponse


def coba(request):
	#return HttpResponse('<h1>coba</h1>')
	name=request.GET.get('name','word')
	# name=request.GET['name']
	return render(request, 'hello/index.html',{'name':name})