from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.urls import reverse
from . import models

data_categories = {
        'data': [
            {'title': 'Food', 'desc': 'Food, water and other you need to staying alive.', 'important': True},
            {'title': 'Utilities', 'desc': 'Water payments, light payments etc', 'important': True},
            {'title': 'Accumulations', 'desc': 'Save up for something', 'important': True},
            {'title': 'Other', 'desc': 'For unexpected things', 'important': False},
        ]
    }

def show_costs(request): 
    return render(request, 'costs/costs.html')


def show_costs_category(request, category_name):
    if category_name == 'redirect':
        url = reverse('category', args=('important', ))
        # print(url)
        return HttpResponseRedirect(url)

    category_info = {}
    for category in data_categories['data']:
        if category['title'] == category_name:
            category_info = {
                'info': category,
                'was_found': True,
            }   
    return render(request, 'costs/category.html', context=category_info)

def show_categories(request):
    return render(request, 'costs/categories.html', context=data_categories)
    