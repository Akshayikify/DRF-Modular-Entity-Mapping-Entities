from rest_framework import serializers
from .models import ProductCourseMapping

class ProductCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductCourseMapping
        fields="__all__"
    
    def validate(self,data):
        course=data.get("course")
        product=data.get("product")
        
        #Here it prevents the duplicates of course product mapping
        if ProductCourseMapping.objects.filter(
            course=course,
            product=product
        ).exists():
            raise serializers.ValidationError(
                "This product course mapping already exists"
            )
            
        #Ensures there is one primary mapping for each products
        if data.get("primary_mapping"):
             if ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
        ).exists():
                 raise serializers.ValidationError(
                     "product already has a primary mapping"
                 )
        return data