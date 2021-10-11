from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    username= models.IntegerField(
       'codigo estudiante',max_length=15,required=True,unique=True)
    first_name=models.CharField('Nombre de usuario',max_length=20,required=True)
    last_name=models.CharField(
       'apellido del usuario',max_length=20,required=True)
    cedula= models.CharField("cedula del usuario",max_length=10, required=True)
    phone= models.CharField("Telefono del usuario",max_lengt=10, required=True)
    email = models.EmailField(blank=True, null=True)
    Empresa= models.BooleanField("es empresa",default=False)

    

    
    class Meta():
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    
    def str(self):
        return f"{self.username}- {self.fist_name} - {self.last_name}"
    


