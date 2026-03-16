from django.urls import path
from . import views  
urlpatterns = [
    path('',views.ProductCourseMappingListView.as_view()),
    path('<int:pk>/',views.ProductCourseMappingDetailView.as_view())
]