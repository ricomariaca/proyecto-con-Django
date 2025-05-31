from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/crear/', views.crear_paciente, name='crear_paciente'),
    path('pacientes/editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),

    path('contactos/', views.lista_contactos, name='lista_contactos'),
    path('contactos/crear/', views.crear_contacto, name='crear_contacto'),
    path('contactos/editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('contactos/eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
]
