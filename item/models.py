from django.contrib.auth.models import User
from django.db import models

from storages.backends.s3boto3 import S3Boto3Storage

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return str(self.name)




class CustomS3Boto3Storage(S3Boto3Storage):
    location = 'media'

    def get_object_parameters(self, name):
        params = super(CustomS3Boto3Storage, self).get_object_parameters(name)
        if 'ACL' in params:
            del params['ACL']
        return params

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/', blank=True, null=True, storage=CustomS3Boto3Storage())
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0)
    full_description = models.TextField(blank=True, null=True)
    full_description_photo = models.ImageField(upload_to='media/', blank=True, null=True, storage=CustomS3Boto3Storage())
    def __str__(self):
        return str(self.name)

