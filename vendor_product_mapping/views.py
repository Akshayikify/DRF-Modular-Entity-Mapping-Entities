from django.shortcuts import render
from rest_framework.views import APIView
from .models import VendorProductMapping  
from .serializers import VendorProductMappingSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
class VendorProductMappingListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve list of vendors and product mappings"
    )
    def get(self,request):
        vendor_product_mappings=VendorProductMapping.objects.all()
        serializer=VendorProductMappingSerializer(vendor_product_mappings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates new Vendor-Product mapping",
        request_body=VendorProductMappingSerializer
    )
    def post(self,request):
        serializer=VendorProductMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class VendorProductMappingDetailView(APIView):
    def get_obj(self,pk):
        try:
            return VendorProductMapping.objects.get(pk=pk)
        except VendorProductMapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieve Vendor-Product mapping by ID"
    )
    def get(self,request,pk):
        vendor_product_mapping=self.get_obj(pk)
        serializer=VendorProductMappingSerializer(vendor_product_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the Vendor-Product mapping details"
    )
    def put(self,request,pk):
        vendor_product_mapping=self.get_obj(pk)
        serializer=VendorProductMappingSerializer(vendor_product_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the Vendor-Product mapping"
    )
    def delete(self,request,pk):
        vendor_product_mapping=self.get_obj(pk)
        vendor_product_mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the Vendor-Product mapping details"
    )
    def patch(self,request,pk):
        vendor_product_mapping=self.get_obj(pk)
        serializer=VendorProductMappingSerializer(vendor_product_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

