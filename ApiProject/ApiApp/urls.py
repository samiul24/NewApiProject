from django.urls import path
from .views import contact_list, contact_details, CategoryView, SubCategoryView

urlpatterns = [
    path('contact_list/', contact_list),
    path('contact_list/<int:pk>', contact_details),
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('subcategory/', SubCategoryView.as_view()),
]
