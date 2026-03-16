from django.shortcuts import render
from rest_framework.views import APIView
from .models import Course  
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
product_param=openapi.Parameter(
    'product_id',
    openapi.IN_QUERY,
    description="Filter course by product ID",
    type=openapi.TYPE_INTEGER
)
class CourseListCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieves all the Courses.Optionally filter the course by product_id",
        manual_parameters=[product_param]
    )
    def get(self,request):
        courses=Course.objects.all()
        product_id=request.GET.get("product_id")
        if product_id:
            courses=courses.filter(
                productcoursemapping__product_id=product_id
            ).distinct()
        serializer=CourseSerializer(courses,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates the new Course"
    )
    def post(self,request):
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):
    def get_obj(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieves the single Course object by ID"
    )
    def get(self,request,pk):
        course=self.get_obj(pk)
        serializer=CourseSerializer(course)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the course details"
    )
    def put(self,request,pk):
        course=self.get_obj(pk)
        serializer=CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the course"
    )
    def delete(self,request,pk):
        course=self.get_obj(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the course details"
    )
    def patch(self,request,pk):
        course=self.get_obj(pk)
        serializer=CourseSerializer(course,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

