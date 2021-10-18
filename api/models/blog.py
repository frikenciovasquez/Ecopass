from django.db import models
from multiselectfield import MultiSelectField
from .users import User

class Blog (models.Model):

    tag= [
        ("Viaje","Viaje"),
        ("aventura","aventura"),
        ("fauna","fauna"),
        ("paisaje cultural","paisaje"),
        ("exploraracion","explorar"),
        ("naturaleza","naturaleza"),
        ("comida","comida"),
        ("descubrir","descubrir"), 
           ]      
    


    title= models.CharField("Titulo",max_length=30)
    body= models.TextField("cuerpo del blog")
    image=models.ImageField("imagen opcional",blank=False,upload_to="Blog")
    tag= MultiSelectField(choices=tag,max_choices=len(tag),blank=True,null=False)
    region= models.CharField("region",max_length=30)

    usuario= models.ForeignKey("User",related_name="blog_usuario",on_delete=models.CASCADE)

        
    class Meta:
        verbose_name='Entrada del blog'
    
    def str(self):
        return f"{self.title}-{self.tag}"
    
