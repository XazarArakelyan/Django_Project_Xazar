from django.http import HttpResponse
from django.shortcuts import render
from timeit import default_timer


# Create your views here.
def shop_view(request):
    # print(request.path)
    # print(request.method)
    # return HttpResponse('<h1>Hello World!</h1>')
    products = [
        ("Laptop", 999),
        ("Desktop", 1999),
        ("Smartphone", 2999),
    ]
    cities = [
        {"name": "Mumbai", "population": "19,000,000", "country": "India"},
        {"name": "Calcutta", "population": "15,000,000", "country": "India"},
        {"name": "New York", "population": "20,000,000", "country": "USA"},
        {"name": "Chicago", "population": "7,000,000", "country": "USA"},
        {"name": "Tokyo", "population": "33,000,000", "country": "Japan"},
    ]
    timer = {
        'time_running': default_timer(),
        'products': products,
        'cities': cities,
    }
    return render(request, 'myshopapp/index.html', context=timer)