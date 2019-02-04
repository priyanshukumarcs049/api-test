from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myapp.serializers import UserSerializer, GroupSerializer, ProductSerializer
from .models import Product
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProductView(viewsets.ModelViewSet):
   
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Product.objects.create(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)



# def send(request):
#     p = Product(name='khan', address='madhapur')
#     p.save()
#     return HttpResponse("data inserted successfully")


