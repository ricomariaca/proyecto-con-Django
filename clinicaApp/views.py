from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Paciente, ContactoSalud
from .forms import PacienteForm, ContactoSaludForm

# ========================
# VISTAS DE AUTENTICACIÓN
# ========================

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña inválidos'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

# ========================
# CRUD DE PACIENTE
# ========================

@login_required
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

@login_required
def crear_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'crear_paciente.html', {'form': form})

@login_required
def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'editar_paciente.html', {'form': form, 'paciente': paciente})

@login_required
def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'eliminar_paciente.html', {'paciente': paciente})

# ========================
# CRUD DE CONTACTOSALUD
# ========================

@login_required
def lista_contactos(request):
    contactos = ContactoSalud.objects.all()
    return render(request, 'lista.html', {'contactos': contactos})

@login_required
def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoSaludForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoSaludForm()
    return render(request, 'formulario.html', {'form': form})

@login_required
def editar_contacto(request, pk):
    contacto = get_object_or_404(ContactoSalud, pk=pk)
    if request.method == 'POST':
        form = ContactoSaludForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoSaludForm(instance=contacto)
    return render(request, 'formulario.html', {'form': form})

@login_required
def eliminar_contacto(request, pk):
    contacto = get_object_or_404(ContactoSalud, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'confirmar_eliminar.html', {'contacto': contacto})
