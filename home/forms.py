from django import forms
from django.contrib.auth.models import User
from .models import Profile,Neighbourhood,Business,Posts
    
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
    fields = ['name','location','population','police_contact','health_contact']
    
#Businesses form
class BusinessForm(forms.ModelForm): 
  class Meta: 
    model = Business
    fields = ['name','phone_number','email','description','image']
    
#Posts form
class PostsForm(forms.ModelForm): 
  class Meta: 
    model = Posts
    fields = ['title','details']
  
#Subscribers form  
class HoodSubscribersForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')