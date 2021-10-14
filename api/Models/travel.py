from django.db import models
from .users import User

class Travel (models.Model):

    transporte=[
       ("avion" , "Aereo"),
        ("bus" ,"terrestre"),
        ("barco", "maritimo"),  
    ]

    
    date_start=models.DateField('fecha de inicio',null=False, default=date.today())
    date_end=models.DateField('fecha de fin',null=False, default=date.today())
    transporte= models.CharField(
        "medio de transporte",choices=transporte, null=False, max_length=32)
    
    user=models.ForeignKey("user",related_name="usuario",on_delete=models.CASCADE)
    
    cotizacion= models.IntegerField("valor del viaje", max_length=10,required=True)

    
    class Meta:
        verbose_name='Viaje'
        verbose_name_plural='Viajes'
    
    def str(self):
        return f"{self.date_start}"
    

