from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SubmitNeighborhood, SubmitAlteredParameters


def start(request):
    res = None
    context = {}

    if request == 'GET':
        # Create form instance and populate it with data from the request
        select_neighborhood_form = SubmitNeighborhood(request.GET)

        neighborhood_code = select_neighborhood_form.cleaned_data['neighborhood_code']

        current_neighborhood_data = fetch_current_data(neighborhood_code)
    else:
        select_neighborhood_form = SubmitNeighborhood()
    
    context['select_neighborhood_form'] = select_neighborhood_form

    return render(request, 'index.html', context)


def start_part2(request):
    select_neighborhood_form = SubmitNeighborhood()
    neighborhood_data = []
    alter_form = SubmitAlteredParameters()

    context = {'select_neighborhood_form': select_neighborhood_form,
               'neighborhood_data': neighborhood_data,
               'alter_form': alter_form
               }

    return render(request, 'alter.html', context)
