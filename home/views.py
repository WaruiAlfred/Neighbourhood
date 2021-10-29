from django.shortcuts import render

# Create your views here.
def home(request): 
  '''Function rendering the homepage'''
  return render(request,'index.html')