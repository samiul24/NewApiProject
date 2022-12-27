from django.db import models
from .model_base import BaseModel
from django.db.models import F

# Create your models here.

class Contact(BaseModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)

    def __str__(self) -> str:
        return f"Name: {self.name}, Title: {self.title}"


class CategoryManager(models.Manager):
    def create_category(self, data):
        # print(data) OrderedDict([('name', 'Meat'), ('is_active', 'True')])
        # print(type(data)) <class 'collections.OrderedDict'>
        # https://docs.djangoproject.com/en/4.1/topics/db/queries/#creating-objects
        return self.create(**data) # its return value is like --> 15, Medicine8, True
    
    def get_category_list(self):
        return self.filter(is_active=True).values('id', 'name', 'is_active') 

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.CharField(max_length=5, default=True)
    objects = CategoryManager()

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.pk, self.name, self.is_active)


class SubCategoryManager(models.Manager):
    def create_sub_category(self, data):
        return self.create(**data)
    
    def get_sub_category_list(self):
        return self.filter(is_active=True)\
            .annotate(category=F('category__name'))\
            .values('category', 'id', 'name', 'is_active')


class SubCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    is_active = models.CharField(max_length=5, default=True)
    objects = SubCategoryManager()

    def __str__(self) -> str:
        return "{}, {}, {}, {}".format(self.category, self.pk, self.name, self.is_active)
