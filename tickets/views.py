from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ticket, Cliente
from .forms import TicketForm, ClienteForm

def index(request):
    return render(request, 'index.html')

def anadirTickets(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket añadido con éxito.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = TicketForm()
    return render(request, 'anadirTickets.html', {'form': form})

def clienteEnEspera(request):
    tickets = Ticket.objects.filter(atendido=False)
    return render(request, 'clienteEnEspera.html', {'tickets': tickets})

def clienteAtendidos(request):
    tickets = Ticket.objects.filter(atendido=True)
    return render(request, 'clienteAtendidos.html', {'tickets': tickets})

def agregarTickets(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente añadido con éxito.')
            return redirect('agregarTickets')
        else:
            messages.error(request, 'Por favor, corrija los errores a continuación.')
    else:
        form = ClienteForm()
    return render(request, 'agregarTickets.html', {'form': form})

def verCliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    tickets = Ticket.objects.filter(cliente=cliente)
    return render(request, 'verCliente.html', {'cliente': cliente, 'tickets': tickets})




    # if request.method == 'POST':
    #     form = TicketForm(request.POST)
    #     if form.is_valid():
    #         cliente = Cliente.objects.get_or_create(nombre=form.cleaned_data['nombre'], 
    #                                               email=form.cleaned_data['email'])
    #         ticket = Ticket.objects.create(cliente=cliente, 
    #                                       descripcion=form.cleaned_data['descripcion'], 
    #                                       prioridad=form.cleaned_data['prioridad'])
    #         return redirect('ver_ticket', ticket_id=ticket.id_ticket)
    # else:
    #     form = TicketForm()
    # return render(request, 'index.html', {
    #     'form': form
    #     })


# # Vista para ver el ticket actual
# def ver_ticket_actual(request):
#     try:
#         ticket_actual = Ticket.objects.filter(atendido=False).order_by('fecha_creacion')[0]
#     except IndexError:
#         ticket_actual = None
#     return render(request, 'tickets_app/ver_ticket_actual.html', {'ticket': ticket_actual})

# # Vista para atender el ticket actual
# def atender_ticket(request, ticket_id):
#     try:
#         ticket = Ticket.objects.get(id_ticket=ticket_id)
#         if not ticket.atendido:
#             ticket.atendido = True
#             ticket.save()
#             return redirect('ver_ticket_actual')
#     except Ticket.DoesNotExist:
#         pass
#     return redirect('ver_ticket_actual')

# # Funciones adicionales para implementar (no incluidas en este ejemplo):

# # Guardar estado de la cola en un archivo
# def guardar_estado_cola(tickets):
#     pass
#     # Implementar la lógica para guardar la lista de tickets en un archivo

# # Cargar estado de la cola desde un archivo
# def cargar_estado_cola():
#     pass
#     # Implementar la lógica para cargar la lista de tickets desde un archivo

# # Ordenar tickets por prioridad
# def ordenar_por_prioridad(tickets):
#     pass
#     # Implementar la lógica para ordenar la lista de tickets por prioridad

# # Buscar ticket por ID
# def buscar_ticket_por_id(ticket_id, tickets):
#     pass
#     # Implementar la lógica para buscar un ticket específico por su ID en la lista

# # Buscar ticket por nombre del cliente
# def buscar_ticket_por_nombre_cliente(nombre_cliente, tickets):
#     pass
#     # Implementar la lógica para buscar tickets por el nombre del cliente en la lista
