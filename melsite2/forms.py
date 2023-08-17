from django import forms
from django.db import models 

class FreqForm(forms.Form):
    cityvalname  = forms.CharField(label="cityvalue", max_length=200)
    freq_val = forms.FloatField()
    rf_pred = forms.FloatField()
