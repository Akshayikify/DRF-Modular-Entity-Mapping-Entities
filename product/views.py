from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product  
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

vendor_param=openapi.Parameter(
    'vender_id',
    openapi.IN_QUERY,
    description="Filter products by vendor ID",
    type=openapi.TYPE_INTEGER
)
class ProductListCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieves list of products. The products are filtered by the vendor by using vendor_id",
        manual_parameters=[vendor_param]
    )
    def get(self,request):
        products=Product.objects.all()
        vendor_id=request.GET.get("vendor_id")
        if vendor_id:
            products=products.filter(
                venderproductmapping__vendor_id=vendor_id
            ).distinct()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates new product"
    )
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_obj(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieves single product object by ID"
    )
    def get(self,request,pk):
        product=self.get_obj(pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the product details"
    )
    def put(self,request,pk):
        product=self.get_obj(pk)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the product"
    )
    def delete(self,request,pk):
        product=self.get_obj(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the product details"
    )
    def patch(self,request,pk):
        product=self.get_obj(pk)
        serializer=ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

