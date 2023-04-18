from django.db import models

# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    text = models.CharField(max_length=100,null=True, blank=True)
    img = models.ImageField(upload_to='parse/images/', null=True, blank=True)
    img_url = models.URLField(null=True, blank=True)
