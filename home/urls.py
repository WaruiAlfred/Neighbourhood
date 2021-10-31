from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'), 
  path('hood/registration/',views.input_hood,name='hood'),
  path('profile/<int:user_id>/',views.profile,name='profile'),
  path('businesses/',views.businesses,name='businesses'),
  path('business/create/',views.create_business,name='create_business'),
  path('search/business/',views.search_business,name='search_business'),
  path("posts/create",views.create_post, name='create_post'),
  path('posts/',views.posts,name='posts'),
  path('search/post/',views.search_post,name='search_post'),
]
