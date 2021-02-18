from django.db import models
from solo.models import SingletonModel
# Create your models here.

class Logo(SingletonModel):
    logo= models.ImageField(upload_to='logo',null=False)
    class Meta:
        verbose_name = "Company Logo"


class Title(SingletonModel):
    name= models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = "Company Title"



class Address(SingletonModel):
    
    
    phone=models.CharField(max_length=15, null=False)
    whatsapp = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=100, null=False)
    office_address= models.TextField()

    class Meta:
        verbose_name = "Company Address"

    
class  SocialSettings(SingletonModel):
    facebook = models.CharField(max_length=255, blank=False)
    linkedin = models.CharField(max_length=255, blank=False)
    twitter = models.CharField(max_length=255, blank=False)
    instagram = models.CharField(max_length=255, blank=False)
    youtube = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = "Social Setting"


class SEO(SingletonModel):
    meta_description= models.TextField(null=False)
    meta_keywords= models.TextField(null=False)
    google_analytics= models.TextField(null=False)

    class Meta:
        verbose_name = "SEO"