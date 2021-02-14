from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel

# Create your models here.
class Slider(models.Model):
    
    title= models.CharField(max_length=100, null=False)
    caption=models.CharField(max_length=255, null=False)
    link = models.CharField(null=True, max_length=255, blank=True)
    slider_image= models.ImageField(upload_to='slider',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class About(SingletonModel):
    
    title= models.CharField(max_length=100, null=False)
    caption=models.CharField(max_length=255, null=False)
    details = RichTextUploadingField()
    tour_done = models.IntegerField(null=False)
    years = models.IntegerField(null=False)
    happy_client = models.IntegerField(null=False)
    cover_image= models.ImageField(upload_to='about',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return "About"

    class Meta:
        verbose_name = "About"
    