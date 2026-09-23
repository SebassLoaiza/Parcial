from django.db import models


class Consola(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre