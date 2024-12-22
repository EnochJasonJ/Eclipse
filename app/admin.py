from django.contrib import admin
from .models import ProductModel, UserModel, OrderModel
# Register your models here.
admin.site.register(ProductModel)
admin.site.register(UserModel)
admin.site.register(OrderModel)