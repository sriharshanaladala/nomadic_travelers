from django.shortcuts import render
from django.http import HttpResponse

places_list = [
    {
        'id': '1',
        'place_name': 'GOA',
        'Description': 'Famous for its pristine beaches, hippie vibes, laidback lifestyle and vibrant parties.',
        'Best_time_to_visit': 'November to February',
        'Ideal_duration': '4-5 days'
    },
    {
        'id': '2',
        'place_name': 'AGRA',
        'Description': 'Say Agra and the first thing that comes to mind is the magnific'
                       'ent Taj Mahal, one of the Seven Wonders of the World.',
        'Best_time_to_visit': 'October to March',
        'Ideal_duration': '2days'
    },
    {
        'id': '3',
        'place_name': 'RAJASTHAN',
        'Description': 'The land of kings, Rajasthan is a vibrant state that attracts history buffs,'
                       ' architecture lovers, wildlife enthusiasts and foodies alike.',
        'Best_time_to_visit': 'November to February',
        'Ideal_duration': '6-7 days'
    },
    {
        'id': '4',
        'place_name': 'DELHI',
        'Description': 'New Delhi, the national capital of India, '
                       'is one of the most cliched yet popular tourist destinations in the country.',
        'Best_time_to_visit': 'October to March',
        'Ideal_duration': '4-5 days'
    },
    {
        'id': '5',
        'place_name': 'MUNNAR',
        'Description': 'Nestled in the Western Ghats in the state of Kerala,'
                       ' Munnar is counted among the most serene and beautiful places to visit in India.',
        'Best_time_to_visit': 'September to March',
        'Ideal_duration': '3-4 days'
    },
    {
        'id': '6',
        'place_name': 'COORG',
        'Description': 'Surrounded by majestic mountain ranges and boasting a lush green landscape,'
                       ' Coorg or Kodagu is yet another cliched holiday destination that is worth the hype.',
        'Best_time_to_visit': 'October to June',
        'Ideal_duration': '3-4 days'
    },

]


def nomads(request):
    msg = "hello you are in the project page"
    context={'msg':msg,'places':places_list}
    return render(request, 'nomads/nomads.html', context)


def nomad(request, pk):
    return render(request, 'nomads/nomad.html')
