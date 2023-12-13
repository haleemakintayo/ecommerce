from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'datetime', 'no_of_people', 'special_request']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input', 'placeholder': 'Date & Time', 'data-target': '#date3', 'data-toggle': 'datetimepicker'}),
            'no_of_people': forms.Select(attrs={'class': 'form-select'}),
            'special_request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Special Request', 'style': 'height: 100px'}),
        }
