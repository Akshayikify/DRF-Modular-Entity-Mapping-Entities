from django.shortcuts import render
from rest_framework.views import APIView
from .models import ProductCourseMapping  
from .serializers import ProductCourseMappingSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
class ProductCourseMappingListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve list of Products and Courses mappings"
    )
    def get(self,request):
        product_course_mappings=ProductCourseMapping.objects.all()
        serializer=ProductCourseMappingSerializer(product_course_mappings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates a new Product Course Mapping",
        request_Body=ProductCourseMappingSerializer
    )
    def post(self,request):
        serializer=ProductCourseMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductCourseMappingDetailView(APIView):
    def get_obj(self,pk):
        try:
            return ProductCourseMapping.objects.get(pk=pk)
        except ProductCourseMapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieve the Products and Courses mapping by ID"
    )
    def get(self,request,pk):
        product_course_mapping=self.get_obj(pk)
        serializer=ProductCourseMappingSerializer(product_course_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the Product-Course mapping details"
    )
    def put(self,request,pk):
        product_course_mapping=self.get_obj(pk)
        serializer=ProductCourseMappingSerializer(product_course_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the Product-Course Mapping"
    )
    def delete(self,request,pk):
        product_course_mapping=self.get_obj(pk)
        product_course_mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the Product-Course mapping details"
    )
    def patch(self,request,pk):
        product_course_mapping=self.get_obj(pk)
        serializer=ProductCourseMappingSerializer(product_course_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

