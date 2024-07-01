from django.urls import path
from .views import crear_ticket, ver_ticket_actual, atender_ticket

urlpatterns = [
    path('crear_ticket/', crear_ticket, name='crear_ticket'),
    path('ver_ticket_actual/', ver_ticket_actual, name='ver_ticket_actual'),
    path('atender_ticket/<int:ticket_id>/', atender_ticket, name='atender_ticket'),
]
