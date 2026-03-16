from django.urls import path
from . import views  
urlpatterns = [
    path('',views.VendorListCreateView.as_view()),
    path('<int:pk>/', views.VendorDetailView.as_view()),
]