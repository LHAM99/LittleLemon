from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from . import views
from rest_framework.authtoken.views import obtain_auth_token 
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/', views.menuView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    #path('booking/', views.BookingViewSet, name='booking'),
    path('api-token-auth/', obtain_auth_token),
]