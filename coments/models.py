from django.db import models
from places.models import Place

# Create your models here.
class Coment(models.Model):
    place=models.ForeignKey(Place, on_delete=models.CASCADE)
    coment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table='coments'
    def __str__(self):
        return self.comment
