from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clienteEnEspera/', views.clienteEnEspera, name='clienteEnEspera'),
    path('clienteAtendidos/', views.clienteAtendidos, name='clienteAtendidos'),
    # path('ver_ticket_actual/', ver_ticket_actual, name='ver_ticket_actual'),
    # path('atender_ticket/<int:ticket_id>/', atender_ticket, name='atender_ticket'),
]
