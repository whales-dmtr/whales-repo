from django.shortcuts import render
from . import models

def show_buys(request):
    buys_data = models.Buys.objects.all()
    print(models.Buys.objects.get(id=1).owner_id)
    return render(request, 'buys/buys.html', {'buys': buys_data})
