from django.shortcuts import render,redirect

# Create your views here.
def index(request):
	return render(request,'index.html',{})

def content(request):
	return render(request,'content.html',{})

def profile(request):
	return render(request,'profile.html',{})

def purchase(request):
	return render(request,'purchase.html',{})