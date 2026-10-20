from django.db import models

# Create your models here.
class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    plan = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.plan})"