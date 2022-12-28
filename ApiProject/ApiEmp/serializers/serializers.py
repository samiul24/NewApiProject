from rest_framework import fields, serializers
from django.db.models import Count
from ApiEmp.models.models import District, Thana, Department, Designation, EmpBasicInfo

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
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Designation
        fields='__all__'


class EmpBasicInfoSerialiser(serializers.ModelSerializer):
    district=DistrictSerializer()
    thana=ThanaSerializer()
    department=DepartmentSerializer()
    designation=DesignationSerializer()
    class Meta:
        model=EmpBasicInfo
        fields=[
                    'id','emp_id','first_name', 'last_name', 
                    'dob', 'phone', 'email', 
                    'thana', 'district', 'joiningdate', 
                    'department', 'designation', 'status'
        ]
        #depth=2