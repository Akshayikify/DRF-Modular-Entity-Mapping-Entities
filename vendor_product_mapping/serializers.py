from rest_framework import serializers
from .models import VendorProductMapping

class VendorProductMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model=VendorProductMapping
        fields="__all__"
    def validate(self,data):
        vendor=data.get("vendor")
        product=data.get("product")
        
        #Here it prevents the duplicates of Vendor product mapping
        if VendorProductMapping.objects.filter(
            vendor=vendor,
            product=product
        ).exists():
            raise serializers.ValidationError(
                "This Vendor product mapping already exists"
            )
            
        #Ensures there is one primary mapping for each vendors
        if data.get("primary_mapping"):
             if VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
        ).exists():
                 raise serializers.ValidationError(
                     "Vendor already has a primary mapping"
                 )
        return data
    