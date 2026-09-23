from django.db import models


class Consola(models.Model):
    TIPOS_CONSOLA = [
        ('Xbox', 'Xbox'),
        ('Play 1', 'Play 1'),
        ('Dreamcast', 'Dreamcast'),
    ]

    nombre = models.CharField(
        max_length=50,
        choices=TIPOS_CONSOLA,
        unique=True
    )

    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} - {self.cantidad} disponibles"


class Reserva(models.Model):
    cliente = models.CharField(max_length=100)
    correo = models.EmailField()
    consola = models.ForeignKey(
        Consola,
        on_delete=models.CASCADE,
        related_name='reservas'
    )
    cantidad = models.PositiveIntegerField(default=1)
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.consola.nombre}"