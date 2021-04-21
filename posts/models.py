from django.db import models
from helpers.models import TrackingModel
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='uploads/blogs/%m')
    # content = models.TextField()
    content = RichTextUploadingField()
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Program(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    director = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length=255)
    summary = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Event(TrackingModel):
    event_date = models.DateTimeField()
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    organizer = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)
    description = models.TextField()
    program = models.ForeignKey(to=Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Person(models.Model):
    ROLE_CHOICES = [
        ('Founder', 'Founder'),
        ('Program Director', 'Program Director'),
        ('Manager', 'Manager'),
        ('Member', 'Member')
    ]
    SALUTATIONS = [
        ('Ms', 'Ms'),
        ('Mr', 'Mr'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof')
    ]
    salutation = models.CharField(
        max_length=10, choices=SALUTATIONS, blank=True, null=True)
    role_choice = models.CharField(
        max_length=20, choices=ROLE_CHOICES, blank=True, null=True)
    fullname = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    bio_pic = models.ImageField(
        blank=True, null=True, upload_to='uploads/people/')
    bio = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self.fullname
