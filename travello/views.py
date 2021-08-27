from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dhaka = Destination()
    dhaka.name = 'Dhaka'
    dhaka.desc = 'dhaka is a beautiful city in Bangladesh'
    dhaka.price = 7100

    chittagong = Destination()
    chittagong.name = 'Chittagong'
    chittagong.desc = 'Chittagong is a beautiful business city in our country'
    chittagong.price = 1100

    jessore = Destination()
    jessore.name = 'Jessore'
    jessore.desc = 'Jessore is a historic city in Bangladesh'
    jessore.price = 7900
    return render(request, 'index.html', {'dhaka' : dhaka, 'chittagong' : chittagong, 'jessore' : jessore})
