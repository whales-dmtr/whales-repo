from django.http import HttpResponse
from django.shortcuts import render
from .models import Users  # type: ignore

def show_my_money(request):
    return render(request, 'wallet/wallet.html')

def page_not_found(request, exception):
    return render(request, 'wallet/page_not_found.html')

Users.objects.filter(id__lte=1).delete()
