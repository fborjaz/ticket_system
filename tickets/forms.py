# from django import forms
# from .models import Ticket

# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ['nombre', 'email', 'descripcion', 'prioridad']

#     def clean_prioridad(self):
#         prioridad = self.cleaned_data['prioridad']
#         if not 1 <= prioridad <= 5:
#             raise forms.ValidationError('La prioridad debe estar entre 1 y 5')
#         return prioridad
