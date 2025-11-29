from django.db import models

# Create your models here.
class Aprendiz(models.Model):
    documento_identificacion = models.CharField(max_length=30, unique=True)
    apellido = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    email = models.EmailField( )
    telefono = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True)
    ciudad = models.CharField(max_length=100 , null=True)
    programa = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido} "
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"