from rest_framework import serializers
from .models import CourseCertificationMapping

class CourseCertificationMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCertificationMapping
        fields="__all__"
    def validate(self,data):
        course=data.get("course")
        certification=data.get("certification")
        
        #Here it prevents the duplicates of course certification mapping
        if CourseCertificationMapping.objects.filter(
            course=course,
            certification=certification
        ).exists():
            raise serializers.ValidationError(
                "This course certification mapping already exists"
            )
            
        #Ensures there is one primary for each courses
        if data.get("primary_mapping"):
             if CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
        ).exists():
                 raise serializers.ValidationError(
                     "course already has a primary mapping"
                 )
        return data