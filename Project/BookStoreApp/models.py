from django.db import models

# Create your models here.

class Authors(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300,unique=True)
    def __str__(self):
        return str(self.Name)


class Shelves(models.Model):
    Name = models.CharField(max_length=50,unique=True) 
    def __str__(self):
        return str(self.Name)
    

class Books(models.Model):
    Title = models.CharField(max_length=50)
    Abstract = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=50 , unique=True)
    author = models.ForeignKey(Authors , on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelves , on_delete=models.CASCADE) 
    def __str__(self):
        return str(self.Title)