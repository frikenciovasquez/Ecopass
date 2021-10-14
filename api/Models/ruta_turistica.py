from django.db import models
from .travel import Travel
from .cotizacion import Cotizacion

class Rute (models.Model):
    
    rute_name= models.CharField(
        "nombre de la ruta turistica", max_length=30,required=True)
    viaje= models.ForeignKey("Travel",related_name="viaje",on_delete=models.CASCADE)

    cotizacion= models.ForeignKey("Cotizacion",related_name="cotizacion",on_delete=models.CASCADE)
    

    class Meta:   
        verbose_name='Ruta'
        verbose_name_plural='Rutas'
    
    
    def str(self):
        return f"{self.rute_name}"