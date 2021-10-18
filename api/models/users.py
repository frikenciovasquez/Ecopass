from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username= models.CharField(
       'nickname del usuario',max_length=15,unique=True)
    first_name=models.CharField('Nombre del usuario',max_length=20)
    last_name=models.CharField(
       'apellido del usuario',max_length=20)
    cedula= models.CharField("cedula del usuario",max_length=10)
    phone= models.CharField("Telefono del usuario",max_length=10)
    email = models.EmailField(blank=True, null=True)
    Empresa= models.BooleanField("es empresa",default=False)

    

    
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    
    def str(self):
        return f"{self.username}- {self.fist_name} - {self.last_name}"
    


