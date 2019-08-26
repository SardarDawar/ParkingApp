from django import forms
from .models import parking_slot as ps


class CarEnterForm(forms.ModelForm):
    class Meta:
        model = ps
        fields = ('car_model','reg_num','slot_no')        
