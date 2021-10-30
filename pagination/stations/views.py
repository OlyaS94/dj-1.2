import csv
from django.urls import reverse
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    csv_path = str(settings.BUS_STATION_CSV)
    DATA = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_station = {
                'Name' : row['Name'], 
                'Street': row['Street'], 
                'District' : row['District']
            }
            DATA.append(bus_station)

    page_number = int(request.GET.get('page', 1))
    element_per_page = 10
    
    paginator = Paginator(DATA, element_per_page)
    page = paginator.get_page(page_number)
    data = page.object_list

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
         'bus_stations': data,
         'page': page
    }
    return render(request, 'stations/index.html', context)
