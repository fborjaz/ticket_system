from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anadirTickets/', views.anadirTickets, name='anadirTickets'),
    path('agregarTickets/', views.agregarTickets, name='agregarTickets'),
    path('clienteEnEspera/', views.clienteEnEspera, name='clienteEnEspera'),
    path('clienteAtendidos/', views.clienteAtendidos, name='clienteAtendidos'),
    path('verCliente/<int:cliente_id>/', views.verCliente, name='verCliente'),
]