from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib import messages

from .models import Profile,Neighbourhood
from .forms import UserUpdateForm,ProfileUpdateForm,NeighbourhoodUpdateForm

# Create your views here.
def home(request): 
  '''Function rendering the homepage'''
  return render(request,'index.html')

def profile(request,user_id): 
  '''Function rendering a logged in user's profile page'''
  user = User.objects.get(id=user_id)
  try:
    profile = Profile.objects.get(user=user.id)
    neighbourhood = Neighbourhood.objects.get(user=user.id)
  except ObjectDoesNotExist: 
    return Http404()
  
  if request.method == 'POST': 
    u_form = UserUpdateForm(request.POST,instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES,instance=profile)
    n_form = NeighbourhoodUpdateForm(request.POST,instance=neighbourhood)
    if u_form.is_valid() and p_form.is_valid() and n_form.is_valid(): 
      u_form.save()
      
      #user neighbourhood
      user_neighbourhood=n_form.save(commit=False)
      user_neighbourhood.user = request.user 
      user_neighbourhood.save()
      
      #user profile
      user_profile=p_form.save(commit=False)
      user_profile.user = request.user 
      user_profile.neighborhood = neighbourhood
      user_profile.save()
      
      messages.success(request,'Your account has been updated!')
      return redirect('profile',user_id=user.id)
  else: 
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=profile)
    n_form = NeighbourhoodUpdateForm(instance=neighbourhood)
  
  context = {
    "profile":profile,
    "neighbourhood":neighbourhood,
    'u_form': u_form,
    'p_form': p_form,
    'n_form': n_form
  }

  return render(request,'registration/profile.html',context)