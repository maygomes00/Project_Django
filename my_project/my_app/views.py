from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm   

# Create your views here.

def home(request):
	return render(request, 'home.html', locals())

def services(request):
	return render(request, 'services.html', locals())

def register(request):
	form = RegisterForm()
	if request.method == 'POST':
		return redirect('home')
	return render(request, 'register.html', locals())

def login(request):
	return render(request, 'login.html', locals())

def contact(request):
	return render(request, 'contact.html', locals())





