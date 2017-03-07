from django.contrib import admin
from .models import List, Card

#register your models to the admin interface
admin.site.register(List)
admin.site.register(Card)