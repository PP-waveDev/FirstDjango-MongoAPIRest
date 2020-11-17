from django.db import models

# Create your models here.
class Tutorial(models.Model):
    titulo = models.CharField(max_length = 70, blank=False, default='')
    descripcion = models.CharField(max_length= 200, blank=False, default='')
    publicado = models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    

