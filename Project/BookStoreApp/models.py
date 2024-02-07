from django.db import models

# Create your models here.
class Books(models.Model):
    Title = models.CharField(max_length=50)
    Abstract = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50 , unique=True)
    Author_ID = models.CharField(max_length=50)
    Shelf_ID = models.CharField(max_length=50) 

class Authors(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300,unique=True)


class Shelves(models.Model):
    Name = models.CharField(max_length=50,unique=True) 
