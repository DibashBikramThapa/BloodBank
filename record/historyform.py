from record.models import History
from django import forms



class HistroyForm(forms.ModelForm):
    class Meta():
        fields=['lastdonateddate',]
        model = History


class BMIForm(forms.Form):
    height_m=forms.FloatField()
    weight_kg=forms.FloatField()
