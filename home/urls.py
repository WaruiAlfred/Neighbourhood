from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'), 
  path('profile/<int:user_id>/',views.profile,name='profile'),
  path('businesses/',views.businesses,name='businesses'),
  path('business/create/',views.create_business,name='create_business'),
  path('search/business/',views.search_business,name='search_business'),
]
