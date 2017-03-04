# 
# ATTN Graders: Some of the structure in this file was inspired
# by the django UI used in PA3
# 

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SubmitNeighborhood, SubmitAlteredParameters
from .data_functions import fetch_current_data, calculate_with_alt_param


def start2(request):
    """
    Show the form to select a neighborhood
    """
    context = {}

    if request.method == 'POST':
        pass
    else:
        select_neighborhood_form = SubmitNeighborhood()
        context['select_neighborhood_form'] = select_neighborhood_form

        return HttpResponseRedirect('/alter/')

    return


def start(request):
    current_neighborhood_data = None
    result2 = None
    context = {}

    if request.method == 'POST':
        # Create form instance and populate it with data from the request
        select_neighborhood_form = SubmitNeighborhood(request.POST)

        neighborhood_code = select_neighborhood_form.cleaned_data['neighborhood_code']
        current_neighborhood_data = fetch_current_data(neighborhood_code)

        return HttpResponseRedirect('/alter/')

    else:
        select_neighborhood_form = SubmitNeighborhood()

    context['select_neighborhood_form'] = select_neighborhood_form
    # context['alter_form'] = alter_form

    return render(request, 'index.html', context)


def start_part2(request):
    context = {}

    if request == 'POST':
        pass
    else:
        alter_form = SubmitAlteredParameters()

    context['alter_form'] = alter_form

    return render(request, 'alter.html', context)
