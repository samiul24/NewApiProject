from rest_framework import fields, serializers
from django.db.models import Count
from ApiEmp.models.models import District, Thana

# Create your serializers here

class DistrictSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = District
        fields = "__all__"

class ThanaSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Thana
        fields = "__all__"