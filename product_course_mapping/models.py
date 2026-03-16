from django.db import models
from course.models import Course
from product.models import Product
class ProductCourseMapping(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    
    primary_mapping=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product}-{self.course}"