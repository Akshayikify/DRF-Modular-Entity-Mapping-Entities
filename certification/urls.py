from django.urls import path
from . import views  
urlpatterns = [
    path('',views.CertificationListCreateView.as_view()),
    path('<int:pk>/',views.CertificationDetailView.as_view())
]