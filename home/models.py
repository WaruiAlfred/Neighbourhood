from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

#Neighbourhood model
class  Neighbourhood(models.Model): 
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  location = models.CharField(max_length=100)
  population = models.IntegerField()
  
  def __str__(self):
    return self.name
  
  def save_neighborhood(self): 
    '''Method to save object instance'''
    self.save()
  
  def delete_neighborhood(self): 
    '''Method to delete object instance'''
    self.delete()
    
  def find_neighborhood(id): 
    '''Method to find neighborhood object instance'''
    neighborhood = Neighbourhood.objects.filter(id=id)
    if neighborhood: 
      return neighborhood
    
  def update_neighborhood(self,id): 
    '''Method to update neighborhood object instance'''
    neighborhood = Neighbourhood.objects.filter(id=id)
    if neighborhood:
      neighborhood.update(name=self.name,location=self.location) 
    
  def update_occupants(self,id): 
    '''Method to update neighborhood object instance population'''
    neighborhood = Neighbourhood.objects.filter(id=id)
    if neighborhood: 
      neighborhood.update(population = self.population)
      
#Profile model
class Profile(models.Model): 
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  bio = models.TextField(max_length=400)
  neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=10)
  public_email = models.EmailField()
  picture = CloudinaryField('profile',blank=True,null=True)
  
  def save_profile(self): 
    '''Funtion to save a profile object'''
    self.save()
  
  def __str__(self):
    return self.user.username
  
#Business model
class Business(models.Model): 
  name = models.CharField(max_length=100)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=10)
  email = models.EmailField()
  description = models.TextField(max_length=1000,blank=True)
  
  def __str__(self):
    return self.name
  
  def save_business(self): 
    '''Method to save business object'''
    self.save()
  
  def delete_business(self): 
    '''Method to delete business object'''
    self.delete()
    
  def find_business(business_id): 
    '''Method to find business according to id'''
    business = Business.objects.filter(id=business_id)
    if business: 
      return business
    
  def update_business(self): 
    '''Method to update business'''
    updated_business = Business.objects.filter(id=self.id).update(name=self.name,
                                                                  user=self.user,
                                                                  neighborhood=self.neighborhood,
                                                                  phone_number=self.phone_number,
                                                                  email=self.email)
    return updated_business
  
#Post model
class Posts(models.Model): 
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  neighborhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  details = models.TextField(max_length=2000)
  date_posted = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  
  def save_post(self): 
    '''Method to save post'''
    self.save()