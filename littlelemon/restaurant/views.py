from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response  
from rest_framework import generics  
# Create your views here.
from django.http import HttpResponse
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
def sayHello(request):
 return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class menuView(APIView):
    
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuItemSerializer(items, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "succes", 
                             "data": serializer.data,
                             })

class bookingView(APIView):
    
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many = True)
        return Response(serializer.data)

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer   
   ### Holi Luis, cuando estes en francia me envias una postal. 
   ### Vaaa.
   
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]