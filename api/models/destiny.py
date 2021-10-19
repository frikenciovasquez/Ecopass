from django.db import models

class Destiny (models.Model):

    tipo_turismo = [
       ("Aventura" , "aventura"),
        ("medicinal" ,"medicinal"),
        ("aves y fauna", "avistamiento"),
        ("empresarial","laboral"),
    ]

    regiones = [
        ("Amazonia","amazonas"),
        ("Andina","andina"),
        ("Caribe","caribe"),
        ("Pacifico","pacifico"),
        ("Orinoquia","orinoquia")
    ]
    nombre= models.CharField("Nombre del destino",max_length=30)
    vacations_type=models.CharField("tipo de destino",choices=tipo_turismo,null=False,max_length=32)
    
    image=models.ImageField(blank=True,upload_to="destiny")
   
    region= models.CharField("locacion",choices=regiones,null=False,max_length=30)
    price=models.IntegerField("precio",null=False,blank=False)
    


     
    

    
    class Meta():  
        verbose_name='Destino'
        verbose_name_plural='Destinos'
    
    def str(self):
        return f"{self.nombre}-{self.location}"
    

