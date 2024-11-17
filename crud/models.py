from django.db import models

class Item(models.Model):
    first_name= models.CharField(max_length=20)
    second_name= models.CharField(max_length=20)
    email= models.EmailField(blank=True, unique=True)
    # image = models.ImageField(upload_to='items/', null=True, blank=True)
    phone= models.CharField(max_length=15)
    description= models.TextField()

    def __str__(self):
        return self.first_name
