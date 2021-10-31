from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404,JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile,Neighbourhood,Business,Posts,HoodSubscribers
from .forms import UserUpdateForm,ProfileUpdateForm,NeighbourhoodUpdateForm,BusinessForm,PostsForm,HoodSubscribersForm

from .email import send_welcome_email

# Create your views here.
def home(request): 
  '''Function rendering the homepage'''
  # form = HoodSubscribersForm()
  if request.method == 'POST': 
    form = HoodSubscribersForm(request.POST)
    if form.is_valid(): 
      name = form.cleaned_data['your_name']
      email = form.cleaned_data['email']
      recipient = HoodSubscribers(name=name,email=email)
      recipient.save()
      send_welcome_email(name,email)
      HttpResponseRedirect('home')
  else: 
    form = HoodSubscribersForm()
  return render(request,'index.html',{"emailForm":form})

def input_hood(request): 
  '''Function that collects user's neighbourhood'''
  if request.method == 'POST': 
    form = NeighbourhoodUpdateForm(request.POST)
    if form.is_valid(): 
      hood = form.save(commit=False)
      hood.user = request.user 
      hood.save_neighborhood()
      return redirect('/')
  else: 
    form = NeighbourhoodUpdateForm()
  return render(request,'hood.html',{"form":form})

@login_required(login_url="/accounts/login/")
def profile(request,user_id): 
  '''Function rendering a logged in user's profile page'''
  f_user = User.objects.get(id=user_id)

  profile = Profile.objects.filter(user=f_user.id).first()
  neighbourhood = Neighbourhood.objects.filter(user=f_user.id).first()

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
      return redirect('profile',user_id=f_user.id)
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

@login_required(login_url="/accounts/login/")
def create_business(request): 
  '''Function to create a new business'''
  neighbourhood = Neighbourhood.objects.get(user=request.user)
  
  if request.method == 'POST': 
    form = BusinessForm(request.POST,request.FILES)
    if form.is_valid(): 
      business = form.save(commit=False)
      business.user = request.user 
      business.neighborhood = neighbourhood
      business.save_business()
    return redirect('businesses')
  else:
    form = BusinessForm() 
  return render(request,'businesses/new_business.html',{"form":form})

@login_required(login_url="/accounts/login/")
def businesses(request): 
  '''Function to display all business in logged in user's neighbourhood'''
  user_neighborhood = Neighbourhood.objects.filter(user=request.user).first()
  businesses = Business.objects.all().filter(neighborhood=user_neighborhood.id)
  print(businesses)
  return render(request,'businesses/business.html',{"businesses":businesses,"neighborhood":user_neighborhood})

@login_required(login_url="/accounts/login/")
def search_business(request): 
  '''Function to search for a business'''
  if 'business' in request.GET and request.GET['business']: 
    search_term = request.GET.get('business')
    businesses = Business.find_business(search_term)
    print(businesses)
    return render(request,'businesses/found_businesses.html',{"businesses":businesses})
  else: 
    message="You have to type in a business name"
    
  return render(request,'businesses/found_businesses.html',{"message":message})
    
@login_required(login_url="/accounts/login/")
def create_post(request): 
  '''Function to create add new post'''
  neighbourhood = Neighbourhood.objects.get(user=request.user)
  
  if request.method == 'POST': 
    form = PostsForm(request.POST)
    if form.is_valid(): 
      post = form.save(commit=False)
      post.author = request.user 
      post.neighborhood = neighbourhood
      post.save_post()
    return redirect('posts')
  else:
    form = PostsForm() 
  return render(request,'posts/new_post.html',{"form":form})

@login_required(login_url="/accounts/login/")
def posts(request): 
  '''Function to display all posts in logged in user's neighbourhood'''
  user_neighborhood = Neighbourhood.objects.filter(user=request.user).first()
  posts = Posts.objects.all().filter(neighborhood=user_neighborhood.id)
  print(businesses)
  return render(request,'posts/posts.html',{"posts":posts,"neighborhood":user_neighborhood})

@login_required(login_url="/accounts/login/")
def search_post(request): 
  '''Function to search for a post'''
  if 'post' in request.GET and request.GET['post']: 
    search_term = request.GET.get('post')
    posts = Posts.objects.filter(title=search_term)
    print(posts)
    return render(request,'posts/found_posts.html',{"posts":posts})
  else: 
    message="You have to type in a post title"
    
  return render(request,'posts/found_posts.html',{"message":message})