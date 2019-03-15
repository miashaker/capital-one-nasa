from django import forms
from django.utils.translation import ugettext as _

MEDIA_CHOICES = (
    ('image','image'),
    ('audio', 'audio'),
    )


class SearchForm(forms.Form):
    general = forms.CharField(label='Search', required=False)
    center = forms.CharField(label='NASA Center', required=False)
    description = forms.CharField(label='Description', required=False)
    description_508 = forms.CharField(label='Description (508)', required=False)
    keywords = forms.CharField(label='Keywords (separate with commas)', required=False)
    location = forms.CharField(label='Location', required=False)
    media_type = forms.MultipleChoiceField(choices=MEDIA_CHOICES, label='Search', required=False)
    nasa_id = forms.CharField(label='media NASA ID', required=False)
    photographer = forms.CharField(label='Photographer', required=False)
    secondary_creator = forms.CharField(label='Secondary Creator', required=False)
    title = forms.CharField(label='Title', required=False)
    year_start = forms.IntegerField(label='Start Year', min_value=1920, max_value=2019, required=False)
    year_end = forms.IntegerField(label='End Year', min_value=1920, max_value=2019, required=False)