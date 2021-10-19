from django.db import models
from .travel import Travel
from .destiny import Destiny

class Rute (models.Model):
    
    rute_name= models.CharField(
        "nombre de la ruta turistica", max_length=30)
    viaje= models.ForeignKey("Travel",related_name="ruta_de_viaje",on_delete=models.CASCADE)
    
    ruta_destinos= models.ManyToManyField("Destiny")

    class Meta:   
        verbose_name='Ruta'
        verbose_name_plural='Rutas'
    
    
    def str(self):
        return f"{self.rute_name}"