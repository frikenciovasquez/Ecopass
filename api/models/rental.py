from django.db import models
from .travel import Travel

class Rental (models.Model):

    region= models.CharField("region",max_length=80)
    price= models.IntegerField("precio",null=False, blank=False)
    description= models.CharField("descripcion",max_length=250)
    phone= models.CharField("telefono",max_length=10)

    class Meta:
        verbose_name='alquiler'
        verbose_name_plural='alquileres'
    
    def str(self):
        return f"{self.region}-{self.description}"
    

