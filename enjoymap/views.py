from django.shortcuts import render
from places.models import Location


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
