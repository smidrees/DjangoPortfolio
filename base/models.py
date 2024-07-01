from django.db import models

# Create your models here.
class Profile(models.Model):

    name = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)
    picture = models.ImageField(upload_to='profile/', height_field=None, width_field=None, max_length=None, blank=True)
    about = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    picture = models.ImageField(upload_to="project/", height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    
class Work(models.Model):
    position = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    company = models.CharField(max_length=50)
    description = models.TextField()
    web_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.position

class Education(models.Model):
    title = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    end_date = models.DateField(auto_now=False, auto_now_add=False, default=None)   
    institute = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Certification(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, default=None)   
    institute = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title   



class Language(models.Model):
    language = models.CharField(max_length=50, blank=True, default=None)
    proficiency = models.CharField(max_length=50, blank=True, default="Basic")

    def __str__(self):
        return self.language

class Social(models.Model):
    platform = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=50, blank=True)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.platform

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.email