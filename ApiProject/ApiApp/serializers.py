from rest_framework import serializers
from .models import Contact, Category, SubCategory

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']

class CategorySerializers(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = "__all__"