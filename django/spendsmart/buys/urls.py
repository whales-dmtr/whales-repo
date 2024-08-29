from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_buys),
    path('buys', views.show_buys, name='buys'),
] 