from django.db import models


class Reserva(models.Model):
    nombre_mascota = models.CharField(max_length=100)
    tipo_mascota = models.CharField(max_length=50)
    nombre_dueno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    servicio = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre_mascota} - {self.nombre_dueno}"