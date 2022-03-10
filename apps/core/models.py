from email import message
from unicodedata import name
from django.db import models
from solo.models import SingletonModel
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Slider(models.Model):
    
    title= models.CharField(max_length=100, null=False)
    caption=models.CharField(max_length=255, null=False)
    link = models.CharField(null=True, max_length=255, blank=True)
    slider_image= models.ImageField(upload_to='slider',null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.slider_image.url))

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
        verbose_name = "About Company"

class Service(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    service_icon = models.ImageField(upload_to='services', null=False)
    description = models.TextField()

    class Meta:
        verbose_name = "Our Service"

    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.service_icon.url))


    def __str__(self):
        return self.title
    

class Review(models.Model):
    CHOICES =(("0","Everest"),("1","Annapurna"),("2","Langtang"),("3","Dolpo"))
    name = models.CharField(max_length=100, null=False, blank=False)
    package_name = models.CharField(choices=CHOICES,null=True, blank=True, max_length=2)
    avatar = models.ImageField(upload_to='review', null=False)
    review = models.TextField()

    class Meta:
        verbose_name = "Review"

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    subject = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name