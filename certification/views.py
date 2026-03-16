from django.shortcuts import render
from rest_framework.views import APIView
from .models import Certification  
from .serializers import CertificationSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
course_param=openapi.Parameter(
    'course_id',
    openapi.IN_QUERY,
    description="Filter certifications by course ID",
    type=openapi.TYPE_INTEGER
)
class CertificationListCreateView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieves all the certifications.Optionally filter the certification by using course_id",
        manual_parameters=[course_param]
    )
    def get(self,request):
        certifications=Certification.objects.all()
        course_id=request.GET.get("course_id")
        if course_id:
            certifications=certifications.filter(
                coursecertificationmapping__course_id=course_id
            ).distinct()
        serializer=CertificationSerializer(certifications,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Create a new Certification",
        request_body=CertificationSerializer
    )
    def post(self,request):
        serializer=CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CertificationDetailView(APIView):
    def get_obj(self,pk):
        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    @swagger_auto_schema(
        operation_description="Retrieves the single certification object by ID",
    )
    def get(self,request,pk):
        certification=self.get_obj(pk)
        serializer=CertificationSerializer(certification)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(
        operation_description="Updates the certification details",
    )
    def put(self,request,pk):
        certification=self.get_obj(pk)
        serializer=CertificationSerializer(certification,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    @swagger_auto_schema(
        operation_description="Deletes the certification",
    )
    def delete(self,request,pk):
        certification=self.get_obj(pk)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @swagger_auto_schema(
        operation_description="Updates the certification details",
    )
    def patch(self,request,pk):
        certification=self.get_obj(pk)
        serializer=CertificationSerializer(certification,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

