from django.db import models

# 1. Pacientes
class Paciente(models.Model):
    TIPO_SEXO = [('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')]

    tipo_identificacion = models.CharField(max_length=10)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=TIPO_SEXO)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    correo_electronico = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


# 2. Profesionales
class Profesional(models.Model):
    tipo_identificacion = models.CharField(max_length=10)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    numero_registro = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.especialidad}"


# 4. Diagnósticos
class Diagnostico(models.Model):
    codigo_cie10 = models.CharField(max_length=10)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.codigo_cie10} - {self.descripcion}"


# 6. Medicamentos
class Medicamento(models.Model):
    nombre_comercial = models.CharField(max_length=100)
    principio_activo = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nombre_comercial


# 8. Procedimientos
class Procedimiento(models.Model):
    codigo_cups = models.CharField(max_length=10)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.codigo_cups} - {self.descripcion}"


# 11. Vacunas
class Vacuna(models.Model):
    nombre_vacuna = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100, blank=True, null=True)
    lote = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_vacuna


# 3. Consultas
class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_consulta = models.DateTimeField(auto_now_add=True)
    motivo_consulta = models.TextField()
    diagnostico = models.TextField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.paciente} - {self.fecha_consulta.date()}"


# 5. Diagnósticos por Consulta
class ConsultaDiagnostico(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, blank=True)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('consulta', 'diagnostico')


# 7. Recetas Médicas
class Receta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, blank=True)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.SET_NULL, null=True, blank=True)
    dosis = models.CharField(max_length=50)
    frecuencia = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)


# 9. Procedimientos por Consulta
class ConsultaProcedimiento(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, blank=True)
    procedimiento = models.ForeignKey(Procedimiento, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('consulta', 'procedimiento')


# 10. Signos Vitales
class SignoVital(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.SET_NULL, null=True, blank=True)
    presion_arterial = models.CharField(max_length=10, blank=True, null=True)
    frecuencia_cardiaca = models.IntegerField(blank=True, null=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    saturacion_oxigeno = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    talla = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)


# 12. Vacunas aplicadas
class PacienteVacuna(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    vacuna = models.ForeignKey(Vacuna, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_aplicacion = models.DateField()

    class Meta:
        unique_together = ('paciente', 'vacuna', 'fecha_aplicacion')
