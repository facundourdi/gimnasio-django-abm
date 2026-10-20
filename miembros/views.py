from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Miembro


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado! Ya puedes iniciar sesión.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'miembros/registro.html', {'form': form})




@login_required
def listar_miembros(request):
    miembros = Miembro.objects.all().order_by('-fecha_registro')
    return render(request, 'miembros/listar.html', {'miembros': miembros})


@login_required
def alta_miembro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        plan = request.POST.get('plan')
        
        Miembro.objects.create(nombre=nombre, edad=edad, plan=plan)
        messages.success(request, 'Miembro registrado exitosamente.')
        return redirect('listar_miembros')
        
    return render(request, 'miembros/alta.html')


@login_required
def editar_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    
    if request.method == 'POST':
        miembro.nombre = request.POST.get('nombre')
        miembro.edad = request.POST.get('edad')
        miembro.plan = request.POST.get('plan')
        miembro.save()
        messages.success(request, 'Datos del miembro actualizados.')
        return redirect('listar_miembros')
        
    return render(request, 'miembros/editar.html', {'miembro': miembro})


@login_required
def baja_miembro(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        miembro.delete()
        messages.success(request, 'Miembro eliminado con éxito.')
        return redirect('listar_miembros')
        
    return render(request, 'miembros/confirmar_baja.html', {'miembro': miembro})