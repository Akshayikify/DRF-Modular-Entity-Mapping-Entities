from django.shortcuts import render
from rest_framework.views import APIView
from .models import CourseCertificationMapping  
from .serializers import CourseCertificationMappingSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
class CourseCertificationMappingListView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve list of Course-Certification mappings"
    )
    def get(self,request):
        course_certification_mappings=CourseCertificationMapping.objects.all()
        serializer=CourseCertificationMappingSerializer(course_certification_mappings,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Creates a new Course-Certification mapping",
        request_body=CourseCertificationMappingSerializer
    )
    def post(self,request):
        serializer=CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CourseCertificationMappingDetailView(APIView):
    def get_obj(self,pk):
        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieves the Course-Certification mapping by ID"
    )
    def get(self,request,pk):
        course_certification_mapping=self.get_obj(pk)
        serializer=CourseCertificationMappingSerializer(course_certification_mapping)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the Course-Certification mapping details"
    )
    def put(self,request,pk):
        course_certification_mapping=self.get_obj(pk)
        serializer=CourseCertificationMappingSerializer(course_certification_mapping,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the Course-Certification mapping"
    )
    def delete(self,request,pk):
        course_certification_mapping=self.get_obj(pk)
        course_certification_mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the Course-Certification mapping details"
    )
    def patch(self,request,pk):
        course_certification_mapping=self.get_obj(pk)
        serializer=CourseCertificationMappingSerializer(course_certification_mapping,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

