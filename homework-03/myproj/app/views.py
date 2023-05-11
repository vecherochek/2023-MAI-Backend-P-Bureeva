from django.http import JsonResponse, HttpResponseBadRequest

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def planet(request, planet_id):
    planet_info = {
        'id': 10,
        'name': 'Mercury',
        'mass': '3.285 × 10^23 kg',
        'distance_from_sun': '57.91 million km',
        'number_of_moons': 0
    }
    return JsonResponse(planet_info, safe=False)


@require_http_methods(["GET", "POST"])
def moon(request, moon_id):
    moon_info = {
        'id': 9,
        'name': 'Phobos',
        'planet_id': 1,
        'distance_from_planet': '9,378 km',
        'diameter': '22.2 km',
        'orbital_period': '7 hours 39 minutes'
    }
    return JsonResponse(moon_info, safe=False)


@require_http_methods(["GET", "POST"])
def astronomical_systems(request):
    if request.method == "GET":
        systems = [
            {
                'id': 10,
                'name': 'Solar System',
                'planets': [
                    'Mercury',
                    'Venus',
                    'Earth',
                    'Mars',
                    'Jupiter',
                    'Saturn',
                    'Uranus',
                    'Neptune'
                ]
            },
            {
                'id': 99,
                'name': 'Alpha Centauri System',
                'planets': [
                    'Proxima Centauri b',
                    'Alpha Centauri Bb'
                ]
            }
        ]
        return JsonResponse(systems, safe=False)
    else:
        return HttpResponseBadRequest("ERROR")
