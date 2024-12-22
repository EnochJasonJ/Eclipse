from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics , status
from .serializer import UserSerializer , ProductSerializer , OrderSerializer
from .models import UserModel , ProductModel, OrderModel
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated ,AllowAny
from .permissions import IsSeller
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
# Create your views here.
def hello(request):
    return HttpResponse("Hello")


@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UpdateUserView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field= "pk"




class ListUserView(generics.ListAPIView):
    queryset  = UserModel.objects.all()
    serializer_class = UserSerializer



class CreateProductView(generics.CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated,IsSeller]
    def perform_create(self, serializer):
        seller = self.request.user
        serializer.save(seller=seller)




class UpdateProductView(generics.UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field= 'pk'


class DeleteProduct(generics.DestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field= 'pk'




class ListProductView(generics.ListAPIView):
    queryset  = ProductModel.objects.all()
    serializer_class = ProductSerializer




class orderViewset(generics.CreateAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.perform_create(serializer)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class ListOrders(generics.ListAPIView):
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer




@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username,password=password)

    if user is not None:
        return Response({"message": "Authenticated successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid username/password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        