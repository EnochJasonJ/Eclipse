from django.urls import path
from .views import CreateUserView , ListUserView


urlpatterns = [
    path('create-user/',CreateUserView.as_view(),name="create-user"),
    path('user/',ListUserView.as_view(),name="user"),
]