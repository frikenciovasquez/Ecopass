from django.db import models


class Travel (models.Model):

    transporte[
       ("avion" , "Aereo"),
        ("bus" ,"terrestre"),
        ("barco", "maritimo"),  
    ]

    destiny= models.CharField(
       'elija destino',max_length=30,required=True)
    Date_start=models.DateField('fecha de inicio',null=False, default=date.today())
    Date_end=models.DateField('fecha de fin',null=False, default=date.today())
    transporte= models.CharField(
        "medio de transporte",choices=transporte, null=False, max_length=32)
    
    

    
    class Meta():
        verbose_name='Destino'
        verbose_name_plural='Destino'
    
    def str(self):
        return f"{self.destiny}"
    
BrB

