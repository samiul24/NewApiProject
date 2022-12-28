from django.urls import path, include

from ApiEmp.views.views import DistrictView, ThanaView, DepartmentView, DesignationView, \
                                EmpBasicInfoView

urlpatterns = [
    path('districtentry/',  DistrictView.as_view()),
    path('districts/',  DistrictView.as_view()),
    path('district/<int:pk>/',  DistrictView.as_view()),
    path('districtupdate/<int:pk>/',  DistrictView.as_view()),
    path('districtdelete/<int:pk>/',  DistrictView.as_view()),

    path('thanaentry/', ThanaView.as_view()),
    path('thanas/',  ThanaView.as_view()),
    path('thana/<int:pk>/',  ThanaView.as_view()),
    path('thanaupdate/<int:pk>/',  ThanaView.as_view()),
    path('thanadelete/<int:pk>/',  ThanaView.as_view()),

    path('employess/', EmpBasicInfoView.as_view())


]