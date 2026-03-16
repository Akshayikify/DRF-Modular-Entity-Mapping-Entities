from django.shortcuts import render
from rest_framework.views import APIView
from vendor.models import Vendor  
from .serializers import VendorSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
class VendorListCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve list of vendors"
    )
    def get(self,request):
        vendors=Vendor.objects.all()
        serializer=VendorSerializer(vendors,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates a new vendor"
    )
    def post(self,request):
        serializer=VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VendorDetailView(APIView):
    def get_obj(self,pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieves the single vendor object by ID"
    )
    def get(self,request,pk):
        vendor=self.get_obj(pk)
        serializer=VendorSerializer(vendor)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the vendor details"
    )
    def put(self,request,pk):
        vendor=self.get_obj(pk)
        serializer=VendorSerializer(vendor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the vendor"
    )
    def delete(self,request,pk):
        vendor=self.get_obj(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the vendor details"
    )
    def patch(self,request,pk):
        vendor=self.get_obj(pk)
        serializer=VendorSerializer(vendor,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
