from django.contrib import admin
from .models import Posts,Profile,Business,Neighbourhood

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Posts)
admin.site.register(Profile)
admin.site.register(Business)