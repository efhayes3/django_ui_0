from django import forms
import csv


class SubmitNeighborhood(forms.Form):

    with open('search/nhood_codes_names.csv', 'r') as f:
        reader = csv.reader(f)
        NEIGHBORHOODS = []
        for row in reader:
            NEIGHBORHOODS.append(tuple(row))

    neighborhood_code = forms.ChoiceField(label='Select Neighborhood', choices=NEIGHBORHOODS, required=True)


class SubmitAlteredParameters(forms.Form):
    alt_crime = forms.IntegerField(label='Crime Level')
    alt_school = forms.IntegerField(label='School Quality', min_value=0, max_value=100)
