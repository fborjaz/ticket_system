from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self): 
        return self.nombre

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    prioridad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    atendido = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.cliente.nombre} - {self.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S")}'
