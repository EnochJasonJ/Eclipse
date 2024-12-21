from django.urls import path
from .views import CreateUserView , ListUserView , CreateProductView , ListProductView, orderViewset, UpdateProductView , DeleteProduct , ListOrders, UpdateUserView



urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name="create-user"),
    path('user/',ListUserView.as_view(),name="user"),
    path('create-product/',CreateProductView.as_view(),name="create-product"),
    path('update-product/<int:pk>/',UpdateProductView.as_view(),name="update-product"),
    path('update-user/<int:pk>/',UpdateUserView.as_view(),name="update-user"),
    path('delete-product/<int:pk>/',DeleteProduct.as_view(),name="delete-product"),
    path('products/',ListProductView.as_view(),name="products"),
    path('order-product/',orderViewset.as_view(),name='order-product'),
    path('orders/',ListOrders.as_view(),name='orders')
]