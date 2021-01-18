from django import forms
from .models import *
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	class  Meta:
		model = Post
		fields = '__all__'
		
		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control'}),
			'author': forms.Select(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
				   }


class UpdateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','body']

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
		}