from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterModelForm, ClientForm, RegisterAnimalForm, LoginForm
from django.contrib.auth import authenticate, login as login_user


# Create your views here.

def home(request):
	return render(request, 'home.html', locals())

def services(request):
	return render(request, 'services.html', locals())

def register(request):
	form = RegisterModelForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			if form.save():
				return redirect('home')
	else:
		form = RegisterModelForm()
	return render(request, 'register.html', locals())

def register_animal(request):
	form = RegisterAnimalForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			if form.save():
				return redirect('home')
	else:
		form = RegisterAnimalForm()
	return render(request, 'register_animal.html', locals())



def login(request):
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username = form.cleaned_data['email'], password = form.cleaned_data['password'])
			if user is not None:
				login(request, user)
			else:
				return redirect('home')
	
	return render(request, 'login.html', locals())

def contact(request):
	return render(request, 'contact.html', locals())





