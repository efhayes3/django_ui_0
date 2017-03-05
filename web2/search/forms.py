from django import forms
import csv


class SubmitNeighborhood(forms.Form):

    with open('search/nhood_code_names.csv', 'r') as f:
        reader = csv.reader(f)
        NEIGHBORHOODS = []
        for row in reader:
            NEIGHBORHOODS.append(tuple(row))

    neighborhood_code = forms.ChoiceField(label='Select Neighborhood', choices=NEIGHBORHOODS, required=True)


class SubmitAlteredParameters(forms.Form):
    alt_crime = forms.IntegerField(label='New Crime Level',  min_value=0, required=False)
    alt_school = forms.IntegerField(label='New School Quality', min_value=0, max_value=100, required=False)
    alt_income = forms.IntegerField(label='New Income Level', min_value=0, required=False)
    alt_cta = forms.ChoiceField(label='CTA Station', choices=[(None, ''), (1, 'Yes'), (0, 'No')], required=False)
