from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Consola, Reserva


def home(request):
    consolas = Consola.objects.all()

    return render(
        request,
        'appReservas/home.html',
        {
            'consolas': consolas
        }
    )


def reservar(request, consola_id):
    consola = Consola.objects.get(id=consola_id)

    if request.method == 'POST':

        cliente = request.POST.get('cliente')
        correo = request.POST.get('correo')

        try:
            cantidad = int(request.POST.get('cantidad'))
        except (ValueError, TypeError):
            cantidad = 0

        if not cliente or not correo:
            messages.error(
                request,
                'Por favor completa todos los campos.'
            )
            return redirect('home')

        if cantidad <= 0:
            messages.error(
                request,
                'La cantidad debe ser mayor a 0.'
            )
            return redirect('home')

        if cantidad > consola.cantidad:
            messages.error(
                request,
                'No hay suficientes consolas disponibles.'
            )
            return redirect('home')

        # Crear reserva
        Reserva.objects.create(
            cliente=cliente,
            correo=correo,
            consola=consola,
            cantidad=cantidad
        )

        # Descontar stock
        consola.cantidad -= cantidad
        consola.save()

        messages.success(
            request,
            f'Reserva realizada correctamente. '
            f'{cantidad} unidad(es) de {consola.nombre} reservada(s).'
        )

        return redirect('home')

    return redirect('home')