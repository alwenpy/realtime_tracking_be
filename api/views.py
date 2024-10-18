from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Location 
from real_time_be.producer import send_location_update
from django.http import JsonResponse

def map_view(request):
    return render(request, 'index.html')

@api_view(['POST'])
def update_location(request):
    lat = request.data.get('latitude')
    lng = request.data.get('longitude')
    
    if lat is not None and lng is not None:
        location = Location(latitude=lat, longitude=lng)
        location.save()

        if location.id:
            Location.objects.exclude(id=location.id).delete()

        location_data = {'latitude': lat, 'longitude': lng}
        send_location_update(location_data)

        return Response({"status": "Location updated"}, status=200)
    
    return Response({"status": "Invalid data"}, status=400)

@api_view(['GET'])
def get_latest_location(request):
    try:
        latest_location = Location.objects.latest('created_at')  # Fetch the latest location
        return JsonResponse({
            'latitude': latest_location.latitude,
            'longitude': latest_location.longitude,
            'status': 'Location retrieved successfully.'
        })
    except Location.DoesNotExist:
        return JsonResponse({'latitude': None, 'longitude': None, 'status': 'No latest location stored.'})
