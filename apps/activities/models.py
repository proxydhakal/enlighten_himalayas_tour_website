from django.db import models
from django.urls import reverse
from apps.country.models import Country
from django.utils.text import slugify
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Activity(models.Model):
   
    title =models.CharField(max_length=255, null=False, unique=True, blank=False)
    slogan =models.CharField(max_length=255, null=False, unique=True, blank=False)
    description =RichTextUploadingField()
    country =models.ForeignKey(Country,on_delete=models.SET_NULL, null=True)
    cover_image =models.ImageField(upload_to='activity/',null=True)
    thumbnail_image =models.ImageField(upload_to='activity/thumbnail/',null=True)
    slug = models.SlugField(null=True, max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Activity, self).save(*args, **kwargs)


    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.thumbnail_image.url))

    def get_absolute_url(self):
        return reverse("activity", kwargs={"slug": self.slug})
