from django.shortcuts import render

def show_buys(request):
    return render(request, 'buys/buys.html')
