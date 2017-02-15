from django import forms

class RegisterForm(forms.Form):
	name = forms.CharField(max_length = 100)
	cpf = forms.CharField(max_length = 11)
	street = forms.CharField(max_length = 100)
	num = forms.CharField(max_length = 100)
	district = forms.CharField(max_length = 100)
	city = forms.CharField(max_length = 100)
	phone = forms.CharField(max_length = 100)
	email = forms.EmailField(max_length = 100)
	password = forms.CharField(max_length = 100, widget = forms.PasswordInput)
	
