from django.contrib import admin
from .models import ProductModel, UserModel
# Register your models here.
admin.site.register(ProductModel)
admin.site.register(UserModel)