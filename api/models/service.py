from django.db import models
from .travel import Travel
from .rental import Rental

class Service (models.Model):

    servicios=[
        ("alquiler","alquiler"),
        ("restaurante","restaurante"),
        ("guia","guia")
    ]

    service= models.CharField(
        "tipo de servicio",choices=servicios,null=False,max_length=30)
    
    viaje= models.ForeignKey("Travel",related_name="servicios_de_viaje",on_delete=models.CASCADE)

    servicios_disponibles=models.ManyToManyField("Rental")



    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def str(self):
        return f"{self.service}-{self.alquiler}"
    

