from django.urls import path
from . import views  
urlpatterns = [
    path('',views.VendorProductMappingListView.as_view()),
    path('<int:pk>/',views.VendorProductMappingDetailView.as_view())
]