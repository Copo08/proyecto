from django.db import models

# Create your models here.
class Persona(models.Model):
    name_alias=models.CharField(max_length=56)
    opinion=models.CharField(max_length=256)
    rate=models.CharField(max_length=32)


    class Meta:
        db_table = 'personas'
    
    def __str__(self):
        return self.name

# Create your models here.
