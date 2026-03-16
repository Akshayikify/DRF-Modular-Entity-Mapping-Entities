from django.db import models
from vendor.models import Vendor
from product.models import Product
class VendorProductMapping(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    primary_mapping=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.vendor}-{self.product}"