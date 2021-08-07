from django.db import models

# Create your models here.

class Administrator(models.Model):
    
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=50)
    
    class Meta:
        db_table = "Administrator"

class Library(models.Model):
    
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
   
    class Meta:
        db_table = "Library"

class Reviews(models.Model):

    LibName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50,null=True)
    Reviews = models.CharField(max_length=50)

    class Meta:
        db_table = "Reviews"

    

