from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def iniciar_sesion(request):
    mensaje = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            mensaje = 'Usuario o contraseña incorrectos.'

    return render(
        request,
        'reservas/login.html',
        {'mensaje': mensaje}
    )

@login_required    
def inicio(request):
    return render(request, 'reservas/inicio.html')

@login_required
def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(
        request,
        'reservas/lista_reservas.html',
        {'reservas': reservas}
    )

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm()

    return render(
        request,
        'reservas/crear_reserva.html',
        {'form': form}
    )

@login_required
def editar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('lista_reservas')
    else:
        form = ReservaForm(instance=reserva)

    return render(
        request,
        'reservas/editar_reserva.html',
        {'form': form, 'reserva': reserva}
    )

@login_required
def eliminar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        reserva.delete()
        return redirect('lista_reservas')

    return render(
        request,
        'reservas/eliminar_reserva.html',
        {'reserva': reserva}
    )