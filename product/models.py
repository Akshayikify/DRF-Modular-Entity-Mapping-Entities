from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} created at {self.created_at} , updated at {self.updated_at}"