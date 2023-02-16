from django.db import models


# Create your models here.
class Estudiante(models.Model):
    GRADOS_CURSANTES = (
        ('1', 'Primer grado'),
        ('2', 'Segundo grado'),
        ('3', 'Tercer grado'),
        ('4', 'Cuarto grado'),
        ('5', 'Quinto grado'),
        ('6', 'Sexto grado'),
        ('7', 'Séptimo grado'),
        ('8', 'Octavo grado'),
        ('9', 'Noveno grado'),
        ('10', 'Décimo grado'),
        ('11', 'Undécimo grado'),
    )

    PrimerNombre = models.CharField(max_length=30)
    SegundoNombre = models.CharField(max_length=30)
    PrimerApellido = models.CharField(max_length=30)
    SegundoApellido = models.CharField(max_length=30)
    FechaDeNacimiento = models.DateField()
    GradoCursante = models.CharField(max_length=2, choices=GRADOS_CURSANTES)
    FotoDelEstudiante = models.ImageField(upload_to='fotos_estudiantes/')
