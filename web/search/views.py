# 
# ATTN Graders: Some of the structure in this file was inspiried 
# by the django UI used in PA3
# 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SubmitNeighborhood, SubmitAlteredParameters
from .data_functions import fetch_current_data, calculate_with_alt_param


def start(request):
    current_neighborhood_data = None
    result2 = None
    context = {}

    if request == 'GET':
        # Create form instance and populate it with data from the request
        select_neighborhood_form = SubmitNeighborhood(request.GET)

        neighborhood_code = select_neighborhood_form.cleaned_data['neighborhood_code']
        current_neighborhood_data = fetch_current_data(neighborhood_code)
    else:
        select_neighborhood_form = SubmitNeighborhood()
    

    if current_neighborhood_data == None:
        context['current_neighborhood_data'] = None
        alter_form = None
    else:
        context['current_neighborhood_data'] = current_neighborhood_data
        alter_form = SubmitAlteredParameters()

    context['select_neighborhood_form'] = select_neighborhood_form
    context['alter_form'] = alter_form
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
