from django.contrib import admin
from .models import Contact, Category, SubCategory

# Register your models here.

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(SubCategory)
