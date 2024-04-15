from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

#--------------------Demo above Content----------------------

class DemoContent(models.Model):
    title = RichTextUploadingField()
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to="Media/")
    
#--------------------Schedule Demo Form----------------------
    
class ScheduleDemoForm(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300)
    mail = models.EmailField(max_length=554)
    phone = models.IntegerField()
    
#--------------------FeaturedIn----------------------
    
class FeaturedIn(models.Model):
    image = models.ImageField(upload_to="Media/")
    
#--------------------ThreeEasySteps----------------------    
    
class ThreeEasySteps(models.Model):
    title = RichTextUploadingField()
    desc = RichTextUploadingField()
    
#--------------------ThreeEasyStepsIcons---------------------- 
    
class ThreeEasyStepsIcons(models.Model):
    title = RichTextUploadingField()
    desc = RichTextUploadingField()
    image = models.ImageField(upload_to="Media/")
    
class Testimonial(models.Model):
    title = RichTextUploadingField()
    desc_1 = RichTextUploadingField()
    desc_2 = RichTextUploadingField()
    
class TestimonialSlider(models.Model):
    desc = RichTextUploadingField()
    name = RichTextUploadingField()
    
    
    
    


#----------------------------------------------Workforce Analytics--------------------------------------------

class Benefits_of_worlforce(models.Model):
    head_and_content = RichTextUploadingField()
    