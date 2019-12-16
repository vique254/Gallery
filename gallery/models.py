from django.db import models

# Create your models here.

   
   
class  location(models.Model):
    place = models.CharField(max_length=35)
    def __str__(self):
        return self.place
    
class   category(models.Model):
    name = models.CharField(max_length=30) 
    
class Image(models.Model):
   image_name = models.CharField(max_length=30)
   image_description = models.CharField(max_length=100)
   image_location = models.ForeignKey(location)
   image_category = models.ForeignKey(category)