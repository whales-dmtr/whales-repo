from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_my_money, name='wallet'),
    path('my_wallet', views.show_my_money, name='wallet'),
]