from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel
from django.utils.html import mark_safe

class Destinations(SingletonModel):
    name =models.CharField(max_length=255, blank=False, null=False, unique=True)
    slogan =models.CharField(max_length=255, blank=False, null=False, unique=True)
    cover_image =models.ImageField(upload_to='destination/',null=False,blank=False)
    
    def __str__(self):
        return self.name
    

class Country(models.Model):
   
    name =models.CharField(max_length=255, blank=False, null=False, unique=True)
    country_slogan =models.CharField(max_length=255, blank=False, null=False, unique=True)
    country_highlight =RichTextUploadingField()
    country_detail =RichTextUploadingField()
    thumbnail_image =models.ImageField(upload_to='country/thumbnail/',null=False,blank=False)
    cover_image =models.ImageField(upload_to='country/',null=False,blank=False)
    slug = models.SlugField(null=True, max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Country"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.thumbnail_image.url))

    def get_absolute_url(self):
        return reverse("countrydetail", kwargs={"slug": self.slug})