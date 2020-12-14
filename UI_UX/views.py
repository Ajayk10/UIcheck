from django.shortcuts import render,redirect
from django.views.generic import View
from rest_framework.serializers import Serializer
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.core.serializers import serialize
from .models import *



# Create your views here.

class index(View):
	def get(self,request,*args,**kwargs):
		feeds = PostFeed.objects.all()
		return render(request, 'index.html', {'feeds': feeds})

def content(request):
	return render(request,'content.html',{})

def profile(request):
	return render(request,'profile.html',{})

def purchase(request):
	return render(request,'purchase.html',{})