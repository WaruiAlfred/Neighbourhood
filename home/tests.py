from django.test import TestCase
from .models import Neighbourhood,Business,Posts,Profile
from django.contrib.auth.models import User

# Neighbourhood test class
class NeighbourhoodTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    self.new_user = User(username="trial",email="trial@gmail.com",password="ssup123")
    self.new_user.save()
    self.membly = Neighbourhood(user=self.new_user,
                               name="Membly",
                               location="Thika",
                               population=500,
                               police_contact='0712345678',
                               health_contact="0787654321")
  
  def tearDown(self):
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.membly,Neighbourhood))
  
  def test_save(self):  
    '''Function testing save method'''
    self.membly.save_neighborhood()
    neighbourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighbourhoods) > 0)
    
  def test_delete(self):  
    '''Function testing delete method'''
    self.membly.save_neighborhood()
    self.membly.delete_neighborhood()
    neighbourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighbourhoods) == 0)
    
  def test_find_neighbourhood(self): 
    '''Function testing search function'''
    self.membly.save_neighborhood()
    found_neighbourhood = Neighbourhood.find_neighborhood("Membly")
    self.assertTrue(found_neighbourhood)
    
  def test_update_neighbourhood(self): 
    '''Function testing update function'''
    self.membly.save_neighborhood()
    Neighbourhood.objects.filter(name="Membly").update(name="Ruaka",population=700)
    updated_neighbourhood = Neighbourhood.objects.get(name="Ruaka")
    self.assertEqual(self.membly,updated_neighbourhood)
    
# Profile test class
class ProfileTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    #User instance
    self.new_user = User(username="trial",email="trial@gmail.com",password="ssup123")
    self.new_user.save()
    #Neighbourhood instance
    self.membly = Neighbourhood(user=self.new_user,
                               name="Membly",
                               location="Thika",
                               population=500,
                               police_contact='0712345678',
                               health_contact="0787654321")
    self.membly.save_neighborhood()
    #Profile instance
    self.user_profile = Profile(user=self.new_user,
                          bio="Coding is my cardio",
                          neighborhood=self.membly,
                          phone_number="0712345678",
                          public_email="trial@gmail.com")
  
  def tearDown(self):
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
    Profile.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.user_profile,Profile))
  
  def test_save(self):  
    '''Function testing save method'''
    self.user_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)
    
# Business test class
class BusinessTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    #User instance
    self.new_user = User(username="trial",email="trial@gmail.com",password="ssup123")
    self.new_user.save()
    #Neighbourhood instance
    self.membly = Neighbourhood(user=self.new_user,
                               name="Membly",
                               location="Thika",
                               population=500,
                               police_contact='0712345678',
                               health_contact="0787654321")
    self.membly.save_neighborhood()
    #Business instance
    self.business = Business(name="Mama's Pizza",
                             user=self.new_user,
                             neighborhood=self.membly,
                             phone_number="0712345678",
                             email="mum@gmail.com",
                             description="One stop place to satisfy yourself.")
  
  def tearDown(self):
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
    Business.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.business,Business))
  
  def test_save(self):  
    '''Function testing save method'''
    self.business.save_business()
    businesses = Business.objects.all()
    self.assertTrue(len(businesses) > 0)
    
  def test_delete(self):  
    '''Function testing delete method'''
    self.business.save_business()
    self.business.delete_business()
    businesses = Business.objects.all()
    self.assertTrue(len(businesses) == 0)
    
  def test_find_business(self): 
    '''Function testing search function'''
    self.business.save_business()
    found_business = Business.find_business("Mama's Pizza")
    self.assertTrue(found_business)
    
  def test_update_business(self): 
    '''Function testing update function'''
    self.business.save_business()
    Business.objects.filter(name="Mama's Pizza").update(name="Pizza Inn")
    updated_business = Business.objects.get(name="Pizza Inn")
    self.assertEqual(self.business,updated_business)
    
# Posts test class
class PostTestClass(TestCase): 
  def setUp(self):
    '''Function that runs before other functions'''
    #User instance
    self.new_user = User(username="trial",email="trial@gmail.com",password="ssup123")
    self.new_user.save()
    #Neighbourhood instance
    self.membly = Neighbourhood(user=self.new_user,
                               name="Membly",
                               location="Thika",
                               population=500,
                               police_contact='0712345678',
                               health_contact="0787654321")
    self.membly.save_neighborhood()
    #Post instance
    self.new_post = Posts(author=self.new_user,
                          neighborhood=self.membly,
                          title="Nature",
                          details="We ought to conserve nature as we can't survive without it.")
  
  def tearDown(self):
    User.objects.all().delete()
    Neighbourhood.objects.all().delete()
    Posts.objects.all().delete()
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.new_post,Posts))
  
  def test_save(self):  
    '''Function testing save method'''
    self.new_post.save_post()
    posts = Posts.objects.all()
    self.assertTrue(len(posts) > 0)