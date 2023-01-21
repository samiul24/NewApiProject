from datetime import date
import time
from django.db.models import Case, When, Value, Count, Max, Min, Avg, F, OuterRef, Subquery, Q, FloatField
from django.db.models.functions import StrIndex, Lower, Substr, Cast, Coalesce, LPad, Replace, RowNumber, DenseRank
from django.db.models import Value as V
from django.db.models.expressions import Window


from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from AppLibs.response import prepare_success_response, prepare_error_response

from ApiEmp.models.models import District, Thana, Department, Designation, EmpBasicInfo, EmpSalary
from ApiEmp.serializers.serializers import DistrictSerializer, ThanaSerializer, \
                                            DepartmentSerializer, DesignationSerializer, \
                                            EmpBasicInfoSerialiser



# Create your views here.

class DistrictView(APIView):
    def get(self, request, pk=None):
        if pk is None:
            try:
                districts = District.objects.all()
                # print(type(districts)) # it returns Query Set
                serializer = DistrictSerializer(districts, many=True)
                return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)

            except Exception as ex:
                return Response(prepare_error_response(), status=status.HTTP_400_BAD_REQUEST)
      
        #try:
        
        district = District.objects.get(id=pk)
        #data = EmpBasicInfo.objects.values('first_name','last_name','employees__basicsalary')
        data = EmpSalary.objects.filter(employee=OuterRef('pk'))
        print(data.query)
        # print(type(district)) # it indicates district model
        serializer = DistrictSerializer(district)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        
        #except Exception as ex:
            #return Response(prepare_error_response(), status=status.HTTP_400_BAD_REQUEST)


    
    def post(self, request):
        try:
            serializer = DistrictSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_success_response(serializer.data), status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(prepare_error_response(), status=status.HTTP_406_NOT_ACCEPTABLE)

        
    def put(self, request, pk):
        try:
            district = District.objects.get(id=pk)
            serializer = DistrictSerializer(district, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_success_response(serializer.data), status=status.HTTP_202_ACCEPTED)
        except Exception as ex:
            return Response(prepare_error_response(), status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        district = District.objects.get(id=pk)
        district.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ThanaView(APIView):
    def get_object(self, pk=None):
        if pk is None:
            return Thana.objects.all()

        try:
            return Thana.objects.get(id=pk)
        except Thana.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        thana=self.get_object(pk)
        if pk is None:
            serializer=ThanaSerializer(thana, many=True) #get method a serializer a data keyword use kora jay na
        else:
            serializer=ThanaSerializer(thana)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ThanaSerializer(data=request.data) #post method a serializer a data keyword must use korte hobe
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(prepare_success_response(serializer.data), status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(prepare_error_response(serializer.error), status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        thana=self.get_object(pk)
        serializer=ThanaSerializer(thana, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        thana=self.get_object(pk)
        thana.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DepartmentView(APIView):
    def get(self, request):
        department_list=Department.objects.all()
        serializer=DepartmentSerializer(department_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DesignationView(APIView):
    def get_object(self, pk):
        try:
            return Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        #designation=Designation.objects.get(pk=pk)
        designation=self.get_object(pk)
        serializer=DesignationSerializer(designation)
        return Response(serializer.data)

    def put(self, request, pk):
        designation=Designation.objects.get(pk=pk)
        #designation=self.get_object(pk)
        serializer=DesignationSerializer(designation, request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpBasicInfoView(APIView):
    def get(self, request):
        employess=EmpBasicInfo.objects.all()
        serializer=EmpBasicInfoSerialiser(employess, many=True)
        return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
    
    def post(self, request):
        today=date.today()
        day_month_year_dept_desig=f'{today.day:02}'+f'{today.month:02}'+str(today.year)[2:]+f'{request.data["department"]:02}'+f'{request.data["designation"]:02}'
        try:
            maximum_id=EmpBasicInfo.objects.aggregate(Max('id'))['id__max']
            maximum_id_info=EmpBasicInfo.objects.filter(id=maximum_id).values('emp_id','first_name','last_name','dob')
            for x in maximum_id_info:
                print(x['first_name'])
            print(maximum_id_info)
            #print(type(maximum_id_info))
        except:
            maximum_id=0
        emp_id=maximum_id+1
        print(emp_id)
        request.data["emp_id"]=day_month_year_dept_desig+str(emp_id)

        serializer=EmpBasicInfoSerialiser(data=request.data)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_success_response(serializer.data), status=status.HTTP_201_CREATED)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


