from django.shortcuts import render, redirect

# Create your views here.
def market_add(request):
    return render(request, "market/market_add.html")

def market_detail(request):
    return render(request, "market/market_detail.html")

def market_list(request):
    return render (request, "market/market_list.html")