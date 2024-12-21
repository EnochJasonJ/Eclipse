from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField( default= '')
    mobile = models.IntegerField( default=0)

    def __str__(self):
        return self.username
    



class ProductModel(models.Model):
    productname = models.CharField(max_length=200)
    category = models.CharField(max_length=150)
    seller = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/')