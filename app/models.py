from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.

class UserModelCreation(BaseUserManager):
    def create_user(self, email,username ,password="", **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email,username ,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)


class UserModel(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length=200)
    email = models.EmailField( default= '', unique=True)
    password = models.CharField(max_length=128, default='')
    mobile = models.IntegerField( default=0)
    role = models.CharField(max_length=20,choices=[('seller','Seller'),('customer','Customer')],default='customer')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserModelCreation()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    



class ProductModel(models.Model):
    productname = models.CharField(max_length=200)
    category = models.CharField(max_length=150)
    seller = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img = models.ImageField(upload_to='images/')
    stocks = models.IntegerField(default = 100)


    def __str__(self):
        return self.productname
    


class OrderModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    total_price  = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"Order by {self.user.username} on {self.order_date}"
