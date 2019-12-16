from django.test import TestCase
from .models import Image,location,category

class LocationTestClass(TestCase):
    def setUp(self):
        self.nakuru=location(place='mall')
        
    def test_save_location(self):
        self.nakuru.save_location()
        locations = location.objects.all()
        self.assertTrue(len(locations) > 0)
        
class CategoryTestClass(TestCase):
    def setUp(self):
        self.tour=category(name='trip')
        
    def test_save_location(self):
        self.tour.save_category()
        categories = category.objects.all()
        self.assertTrue(len(categories) > 0)
        
# Create your tests here.
class ImageTestClass(TestCase):
    
    
    def setUp(self):
        self.nakuru=location(place='mall')
        self.tour=category(name='trip')
        self.nakuru.save_location()
        self.tour.save_category()
        
        self.happy = Image(image_name ='happy',image_description ='feeling happy and joyful',image_location=self.nakuru,image_category=self.tour)
        
# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.happy,Image))        