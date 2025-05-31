from django.contrib import admin
from .models import (
    Pais,
    Ciudad,
    Ocupacion,
    Discapacidad,
    Etnia,
    EntidadAdministradora,
    ModalidadAtencion,
    ViaIngreso,
    PrioridadAtencion,
    DiagnosticoCIE10,
    DocumentoIdentidad
)

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('id_pais', 'nombre')
    search_fields = ('id_pais', 'nombre')

@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id_ciudad', 'nombre', 'codigo_dane')
    search_fields = ('id_ciudad', 'nombre', 'codigo_dane')

@admin.register(Ocupacion)
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ('id_ocupacion', 'descripcion', 'id_padre')
    search_fields = ('id_ocupacion', 'descripcion')

@admin.register(Discapacidad)
class DiscapacidadAdmin(admin.ModelAdmin):
    list_display = ('id_discapacidad', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(Etnia)
class EtniaAdmin(admin.ModelAdmin):
    list_display = ('id_etnia', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(EntidadAdministradora)
class EntidadAdministradoraAdmin(admin.ModelAdmin):
    list_display = ('codigo_eapb', 'nombre')
    search_fields = ('codigo_eapb', 'nombre')

@admin.register(ModalidadAtencion)
class ModalidadAtencionAdmin(admin.ModelAdmin):
    list_display = ('id_modalidad', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(ViaIngreso)
class ViaIngresoAdmin(admin.ModelAdmin):
    list_display = ('id_via', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(PrioridadAtencion)
class PrioridadAtencionAdmin(admin.ModelAdmin):
    list_display = ('id_prioridad', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(DiagnosticoCIE10)
class DiagnosticoCIE10Admin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'codigo_padre')
    search_fields = ('codigo', 'descripcion')

@admin.register(DocumentoIdentidad)
class DocumentoIdentidadAdmin(admin.ModelAdmin):
    list_display = ('tipo_documento_codigo', 'nombre_doc')
    search_fields = ('tipo_documento_codigo', 'nombre_doc')
