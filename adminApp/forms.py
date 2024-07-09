from django import forms
class IntegerDateForm(forms.Form):
    integer_value = forms.IntegerField()
    date_value = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

from django import forms
import pytz

class LocationForm(forms.Form):
    timezone = forms.ChoiceField(choices=[(tz, tz) for tz in pytz.all_timezones])