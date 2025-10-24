from django.shortcuts import render
from django.http import JsonResponse
from .models import Location
import json

def map_page(request):
    return render(request, 'maps/map.html')

def save_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        lat = data.get('latitude')
        lng = data.get('longitude')
        if lat and lng:
            Location.objects.create(latitude=lat, longitude=lng)
            return JsonResponse({'message': 'Location saved successfully!'})
        else:
            return JsonResponse({'error': 'Invalid coordinates'}, status=400)
