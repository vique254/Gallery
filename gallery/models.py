from django.db import models

# Create your models here.

   
   
class location(models.Model):
    place = models.CharField(max_length=35)
    def __str__(self):
        return self.place
    
    def save_location(self):
        self.save()
    
class category(models.Model):
    name = models.CharField(max_length=30) 
    
    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save()
        
    
class Image(models.Model):
   image_name = models.CharField(max_length=30)
   image_description = models.CharField(max_length=100)
   image_location = models.ForeignKey(location)
   image_category = models.ForeignKey(category)
   image = models.ImageField(upload_to='images')
   
   @classmethod
   def get_images(cls):
       image=cls.objects.all()
       return image
   
   @classmethod
   def search_by_name(cls,search_term):
        gallery = cls.objects.filter(image_category__name__icontains=search_term)    
        return gallery
    
    