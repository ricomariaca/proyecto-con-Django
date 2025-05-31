from django.db import models


class Pais(models.Model):
    id_pais = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=100)

class Ocupacion(models.Model):
    id_ocupacion = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=100)
    id_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.id_ocupacion} {self.descripcion or ''}".strip()

class Ciudad(models.Model):
    id_ciudad = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=100)
    codigo_dane = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.codigo_dane} {self.nombre or ''}".strip()

class Discapacidad(models.Model):
    id_discapacidad = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=100)

class Etnia(models.Model):
    id_etnia = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id_etnia} {self.descripcion or ''}".strip()

class EntidadAdministradora(models.Model):
    codigo_eapb = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.codigo_eapb} {self.nombre or ''}".strip()

class ModalidadAtencion(models.Model):
    id_modalidad = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id_modalidad} {self.descripcion or ''}".strip()

class ViaIngreso(models.Model):
    id_via = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id_via} {self.descripcion or ''}".strip()

class PrioridadAtencion(models.Model):
    id_prioridad = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.id_prioridad} {self.descripcion or ''}".strip()

class DocumentoIdentidad(models.Model):
    tipo_documento_codigo = models.CharField(primary_key=True, max_length=15)
    nombre_doc = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tipo_documento_codigo} {self.nombre_doc or ''}".strip()




# PACIENTE Y RELACIONES


class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Hombre'),
        ('F', 'Mujer'),
        ('I', 'Intersexual'),

    ]

    GENERO_CHOICES = [
        ('H', 'Masculino'),
        ('M', 'Femenino'),
        ('T', 'Transgenero'),
        ('N', 'Neutro'),
        ('NA', 'No lo declara'),
    ]

    Municipio = [
        ('05440', '05440 - Marinilla'),
        ('05376', '05376 - La Ceja'),
        ('05318', '05318 - Guarne'),
        ('05313', '05313 - Granada'),
        ('05002', '05002 - Abejorral'),
        ('05021', '05021 - Alejandría'),
        ('05055', '05055 - Argelia'),
        ('05148', '05148 - Carmen De Viboral'),
        ('05197', '05197 - Cocorná'),
        ('05206', '05206 - Concepción'),
        ('05321', '05321 - Guatape'),
        ('05400', '05400 - La Unión'),
    ]


    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)
    tipo_documento = models.ForeignKey(DocumentoIdentidad, on_delete=models.DO_NOTHING)
    numero_doc = models.CharField(max_length=20)
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES)
    genero = models.CharField(max_length=15, choices=GENERO_CHOICES)
    fecha_nacimiento = models.CharField(max_length=20)
    hora_nacimiento = models.CharField(max_length=20)
    ciudad_residencia = models.ForeignKey(Ciudad, on_delete=models.DO_NOTHING)
    id_ocupacion = models.ForeignKey(Ocupacion, on_delete=models.DO_NOTHING)
    id_etnia = models.ForeignKey(Etnia, on_delete=models.DO_NOTHING)
    Municipio = models.CharField(max_length=15, choices=Municipio)
    codigo_eapb = models.ForeignKey(EntidadAdministradora, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre or ''} {self.primer_apellido} {self.segundo_apellido or ''}".strip()

class NacionalidadPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('paciente', 'pais')

class PacienteDiscapacidad(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    discapacidad = models.ForeignKey(Discapacidad, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('paciente', 'discapacidad')

class VoluntadAnticipada(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    documento_url = models.TextField()
    fecha_registro = models.DateTimeField()
    se_opone = models.CharField(max_length=15, null=True, blank=True)

class PresuncionDonacion(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    se_opone = models.CharField(max_length=15, null=True, blank=True)
    fecha_registro = models.DateField()

# ======================
# DIAGNÓSTICO Y CONTACTO
# ======================

class DiagnosticoCIE10(models.Model):
    codigo = models.CharField(primary_key=True, max_length=15)
    descripcion = models.CharField(max_length=255)
    codigo_padre = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.codigo} {self.descripcion or ''}".strip()


class ContactoSalud(models.Model):
    Tiraje_CHOICES = [
        ('I', 'Tiraje I'),
        ('II', 'Tiraje II'),
        ('III', 'Tiraje III'),
        ('IV', 'Tiraje IV'),
        ('V', 'Tiraje V'),
    ]

    Entorno_CHOICES = [
        ('1', 'Hogar'),
        ('2', 'Comunitario'),
        ('3', 'Escolar'),
        ('4', 'Laboral'),
        ('5', 'Institucional'),
    ]



    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    fecha_atencion = models.DateTimeField()
    id_modalidad = models.ForeignKey(ModalidadAtencion, on_delete=models.DO_NOTHING)
    id_via = models.ForeignKey(ViaIngreso, on_delete=models.DO_NOTHING)
    id_prioridad = models.ForeignKey(PrioridadAtencion, on_delete=models.DO_NOTHING)
    motivo_atencion = models.TextField()
    entorno = models.CharField(max_length=20, choices=Entorno_CHOICES)
    fecha_hora_triage = models.CharField(max_length=20)
    clasificacion_triage = models.CharField(max_length=20, choices=Tiraje_CHOICES)
    diagnostico_cie10 = models.ForeignKey(DiagnosticoCIE10, on_delete=models.DO_NOTHING)
    codigo_eapb = models.ForeignKey(EntidadAdministradora, on_delete=models.DO_NOTHING)