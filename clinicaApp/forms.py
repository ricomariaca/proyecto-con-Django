from django import forms
from .models import Paciente, ContactoSalud

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        labels = {
            'id_etnia': 'Etnia',
            'id_ocupacion': 'Ocupación',}

class ContactoSaludForm(forms.ModelForm):
    class Meta:
        model = ContactoSalud
        fields = '__all__'
        labels = {
            'id_via': 'Vía de Ingreso',
            'id_prioridad': 'Diagnostico principal de ingreso',
            'id_modalidad': 'Modalidad de Atención',}
