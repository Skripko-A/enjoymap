import json

from django.shortcuts import render
from places.models import Location
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from .settings import MEDIA_ROOT


def show_map(request):
    locations = Location.objects.all()
    features = []
    for location in locations:
        feature = {'type': 'Feature',
                   'geometry': {'type': 'Point', 'coordinates': [location.lng, location.lat]},
                   'properties':
                       {'title': location.title,
                        'placeId': location.place_id,
                        'detailsUrl': location.detailsUrl
                        }
                   }
        features.append(feature)
    places_geojson = {'type': 'FeaturesCollection', 'features': features}

    return render(request, 'show_map.html', context={'places_geojson': places_geojson})


def show_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    image_urls = [str(image.filename) for image in location.image.all()]
    location_json = {
        'title': location.title,
        'imgs': image_urls,
        'description_short': location.description_short,
        'description_long': location.description_long,
        'coordinates': {
            'lat': str(location.lat),
            'lng': str(location.lng)
                     }
        }
    return JsonResponse(location_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
