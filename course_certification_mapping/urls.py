from django.urls import path
from . import views  
urlpatterns = [
    path('',views.CourseCertificationMappingListView.as_view()),
    path('<int:pk>/',views.CourseCertificationMappingDetailView.as_view())
]