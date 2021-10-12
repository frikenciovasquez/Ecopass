from django.db import models


class Destiny (models.Model):

    tipo_turismo[
       ("Aventura" , "aventura"),
        ("medicinal" ,"medicinal"),
        ("aves y fauna", "avistamiento"),
        ("empresarial","laboral"),
    ]

    regiones[
        ("Amazonia","amazonas"),
        ("Andina","andina"),
        ("Caribe","caribe"),
        ("Pacifico","pacifico"),
        ("Orinoquia","orinoquia")
    ]
    nombre= models.CharField("Nombre del destin",max_length=30,required=True)
    vacations_type=models.CharField("tipo de destino",choices=tipo_turismo,null=False,max_length=32)
    destiny= models.CharField(
       'elija destino',max_length=30,required=True)
    image=models.ImageField(blank=False,upload_to="destiny")
    #tag = preguntar a lizardo
    location=models.CharField("locacion del destino",max_length=30,required=True)
    region= models.CharField("locacion",choices=regiones,null=False,max_length=30)
    price=models.IntegerField("precio",null=False,blank=False)
    
    

    
    class Meta():   
        pass
    
    def str(self):
        return f"{self.nombre}-{self.location}"
    

