from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializer import UserSerializer
from .models import UserModel
# Create your views here.
def hello(request):
    return HttpResponse("Hello")



class CreateUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer




class ListUserView(generics.ListAPIView):
    queryset  = UserModel.objects.all()
    serializer_class = UserSerializer