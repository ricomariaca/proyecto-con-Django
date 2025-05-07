from django.contrib import admin
from .models import *


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombres','numero_identificacion', 'tipo_identificacion')
    search_fields = ('numero_identificacion', 'nombres')

admin.site.register(Profesional)
admin.site.register(Consulta)
admin.site.register(Diagnostico)
admin.site.register(ConsultaDiagnostico)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre_comercial','presentacion')
    list_display_links = ('presentacion',)
    list_editable = ('nombre_comercial',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('consulta','medicamento', 'dosis', 'frecuencia', 'duracion')
    search_fields = ('consulta',)

admin.site.register(Procedimiento)
admin.site.register(ConsultaProcedimiento)
admin.site.register(SignoVital)
admin.site.register(Vacuna)
admin.site.register(PacienteVacuna)