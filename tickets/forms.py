from django import forms
from .models import Cliente, Ticket

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']  # Use 'email' for the email field
        labels = {
            'nombre': 'Nombre',  
            'email': 'Correo electrónico',
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['cliente', 'descripcion', 'prioridad']
        labels = {
            'cliente': 'Cliente',
            'descripcion': 'Descripción',
            'prioridad': 'Prioridad',
        }

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['atendido']
        labels = {
            'atendido': '¿Atendido?', 
        }
