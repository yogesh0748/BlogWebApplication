from sys import set_int_max_str_digits

from django.db import models
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # Specify max_length here
    description = models.TextField()
    url = models.CharField(max_length=200)  # Specify max_length here
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:20px;border-radius: 50%" />'.format(self.image))


    def __str__(self):
        return self.title



# Post Model

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)  # Specify max_length here
    content = models.TextField()
    url = models.CharField(max_length=200)  # Specify max_length here
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set on each update


    def __str__(self):
        return self.title

