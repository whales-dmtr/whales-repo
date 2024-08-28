from django.urls import path, register_converter  
from . import views
from . import converters as conv 

register_converter(conv.SpecStr, 'spec_str')

urlpatterns = [
    path('', views.show_costs),
    path('my_costs/', views.show_costs, name='costs'),
    path('category/<spec_str:category_name>', views.show_costs_category, name='category'), 
    path('categories/', views.show_categories, name='all_categories')
]