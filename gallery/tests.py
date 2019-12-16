from django.test import TestCase
from .models import Image,location,category
# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.happy = Image(image_name ='happy',image_description ='feeling happy and joyful',image_location='CBD',image_category= 'walk')
        
# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.happy,Image))        