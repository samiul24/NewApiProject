from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Contact, Category, SubCategory
from .serializers import ContactSerializers, CategorySerializers, SubCategorySerializer
from AppLibs.response import prepare_success_response, prepare_error_response

# Create your views here.
@csrf_exempt
def contact_list(request):
    if request.method =='GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializers(contacts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = ContactSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def contact_details(request, pk):
    try:
        contact = Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=400)
    
    if request.method=='GET':
        serializer = ContactSerializers(contact)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.error, status=400)
    
    elif request.method == 'DELETE':
        contact.delete()
        return HttpResponse(status=204)


# https://realpython.com/python-super/
# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# https://www.youtube.com/watch?v=IlGguIgO5x4

class CategoryView(APIView):
    def __init__(self):
        super(CategoryView, self).__init__() # same as super().__init__()
        self.serializer = CategorySerializers

    def get(self, request):
        try:
            categories = Category.objects.get_category_list()
            # print(categories) # <QuerySet [{'id': 1, 'name': 'Grocary', 'is_active': 'True'}, {'id': 2, 'name': 'Rice', 'is_active': 'True'}]
            # print(type(categories)) # <class 'django.db.models.query.QuerySet'>
            return Response(prepare_success_response(categories), status=status.HTTP_200_OK)
        except:
            return Response(prepare_error_response(), status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        # print(request) <rest_framework.request.Request: POST '/category/'>
        # print(type(request)) <class 'rest_framework.request.Request'>
        # print(request.data) <QueryDict: {'name': ['Medicine10'], 'is_active': ['True']}>
        serializer = self.serializer(data=request.data)
        #print(serializer) CategorySerializers(data=<QueryDict: {'name': ['Medicine1'], 'is_active': ['True']}>):
                                                #id = IntegerField(label='ID', read_only=True)
                                                #name = CharField()
                                                #is_active = CharField(max_length=5, required=False)

        try:
            serializer.is_valid(raise_exception=True)
            print(1)
            # print(serializer.validated_data) OrderedDict([('name', 'Medicine3'), ('is_active', 'True')])
            category = Category.objects.create_category(data=serializer.validated_data)
            # print(category) 15, Medicine8, True
            # print(type(category)) <class 'ApiApp.models.Category'>
            return Response(prepare_success_response(), status=status.HTTP_200_OK)

        except Exception as ex:
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)

class SubCategoryView(APIView):
    def __init__(self):
        super(SubCategoryView, self).__init__()
        self.serializer = SubCategorySerializer
    
    def get(self, request):
        try:
            subcategories = SubCategory.objects.get_sub_category_list()
            subcategories1 = SubCategory.objects.all()
            # print(subcategories) # <QuerySet [{'id': 1, 'name': 'Milk', 'is_active': 'True', 'main_category': 'Grocary'}]>
            # print(subcategories1) # <QuerySet [<SubCategory: 1, Grocary, True, 1, Milk, True>]>
            return Response(prepare_success_response(subcategories), status=status.HTTP_200_OK)
        except:
            return Response(prepare_error_response(), status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = self.serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            subcategory = SubCategory.objects.create_sub_category(data=serializer.validated_data)
            return Response(prepare_success_response(), status=status.HTTP_200_OK)
            
        except Exception as ex:
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)