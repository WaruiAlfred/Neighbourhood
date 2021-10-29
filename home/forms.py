from django import forms
from django.contrib.auth.models import User
from .models import Profile,Neighbourhood
    
#User update form
class UserUpdateForm(forms.ModelForm): 
  class Meta: 
    model = User
    fields = ['username']

#Profile update form
class ProfileUpdateForm(forms.ModelForm): 
  class Meta: 
    model = Profile
    fields = ['phone_number','public_email','bio','picture']
    
#Neighbourhood update form
class NeighbourhoodUpdateForm(forms.ModelForm): 
  class Meta: 
    model = Neighbourhood
    fields = ['name','location','population']