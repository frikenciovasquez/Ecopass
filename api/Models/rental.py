from django.db import models
from .travel import Travel

class Rental (models.Model):

    region= models.CharField("region",max_length=30,required=True)
    price= models.IntegerFIeld("precio",max_length=10,required=True)
    description= models.CharField("descripcion",max_length=250,required=True)
    phone= models.CharField("telefono",max_length=10,required=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def str(self):
        return f"{self.region}-{self.description}"
    

