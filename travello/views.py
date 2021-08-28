from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):
    dhaka = Destination()
    dhaka.name = 'Dhaka'
    dhaka.desc = 'dhaka is a beautiful city in Bangladesh'
    dhaka.img = 'destination_1.jpg'
    dhaka.price = 7100
    dhaka.offer = False

    chittagong = Destination()
    chittagong.name = 'Chittagong'
    chittagong.desc = 'Chittagong is a beautiful business city in our country'
    chittagong.img = 'destination_2.jpg'
    chittagong.price = 1100
    chittagong.offer = True

    jessore = Destination()
    jessore.name = 'Jessore'
    jessore.desc = 'Jessore is a historic city in Bangladesh'
    jessore.img = 'destination_3.jpg'
    jessore.price = 7900
    jessore.offer = False

    dests = [dhaka, chittagong, jessore]
    return render(request, 'index.html', {'dests' : dests})
