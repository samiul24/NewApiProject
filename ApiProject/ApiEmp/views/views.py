from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from AppLibs.response import prepare_success_response, prepare_error_response

from ApiEmp.models.models import District, Thana
from ApiEmp.serializers.serializers import DistrictSerializer, ThanaSerializer

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
      
        try:
            district = District.objects.get(id=pk)
            # print(type(district)) # it indicates district model
            serializer = DistrictSerializer(district)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        
        except Exception as ex:
            return Response(prepare_error_response(), status=status.HTTP_400_BAD_REQUEST)


    
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
