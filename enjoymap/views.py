from django.shortcuts import render
from django.urls import reverse
from places.models import Location
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse


def show_map(request):
    locations = Location.objects.all()
    features = []
    for location in locations:
        feature = {'type': 'Feature',
                   'geometry': {'type': 'Point', 'coordinates': [location.lng, location.lat]},
                   'properties':
                       {'title': location.title,
                        'placeId': location.place_id,
                        'detailsUrl': reverse('location_page', args=f'{location.id}')
                        }
                   }
        features.append(feature)
    places_geojson = {'type': 'FeatureCollection', 'features': features}
    return render(request, 'show_map.html', context={'places_geojson': places_geojson})


def show_location(request, location_id):
    location = get_object_or_404(Location, pk=location_id)
    location_json = {
        'title': location.title,
        'imgs': [f'{image.filename.url}' for image in location.images.all()],
        'description_short': location.description_short,
        'description_long': location.description_long,
        'coordinates': {
            'lat': str(location.lat),
            'lng': str(location.lng)
        }
    }
    return JsonResponse(location_json, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
