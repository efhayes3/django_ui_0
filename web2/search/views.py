from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import SubmitNeighborhood, SubmitAlteredParameters


def home(request):
    """The home page form. Prompts the user to select a neighborhood to analyze."""
    context = {}

    if request.method == 'POST':
        select_form = SubmitNeighborhood(request.POST)
        alter_form = SubmitAlteredParameters(request.POST)

        if form.is_valid():
            neighborhood_code = select_form.cleaned_data['neighborhood_code']
            alt_crime = alter_form.cleaned_data['alt_crime']
            alt_school = alter_form.cleaned_data['alt_school']
            alt_income = alter_form.cleaned_data['alt_income']
            alt_CTA = alter_form.cleaned_data['alt_CTA']

    else:
        select_form = SubmitNeighborhood()
        alter_form = SubmitAlteredParameters()

    context['select_form'] = select_form
    context['alter_form'] = alter_form

    return render(request, 'index.html', context)


def test_forms(request):
    """Shows all the forms."""
    context = {}

    if request.method == 'POST':
        form1 = SubmitNeighborhood(request.POST)
        form2 = SubmitAlteredParameters(request.POST)
    else:
        form1 = SubmitNeighborhood()
        form2 = SubmitAlteredParameters()

    context['form1'] = form1
    context['form2'] = form2

    return render(request, 'test.html', context)