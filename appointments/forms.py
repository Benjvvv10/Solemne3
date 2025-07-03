from django import forms
from .models import Appointment
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        # No es necesario validar aquí si ya lo haces en el modelo
        return cleaned_data