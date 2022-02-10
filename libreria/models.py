from contextlib import nullcontext
from distutils.command.upload import upload
from pyexpat import model
from tkinter import image_names
from django.db import models

# Create your models here.

class libro(models.Model):

    id = models.AutoField(primary_key=True)
    cantidad = models.CharField(max_length=100, verbose_name='Cantidad',null=True)
    crecedora = models.CharField(max_length=100, verbose_name='Crecedora',null=True)
    engordadora = models.CharField(max_length=100, verbose_name='Engordadora',null=True)
    inversion = models.CharField(max_length=100, verbose_name='Inversion',null=True)
    image = models.ImageField(upload_to='imagenes/',verbose_name='Image' ,null=True)
    descripcion = models.TextField(max_length=100, verbose_name='Descripcion',null=True)
    total = models.CharField(max_length=100, verbose_name='Total',null=True)

    def __str__(self):
       fila = "Cantidad: " + self.cantidad + "_" + "Crecedora: " + self.crecedora + "Engordadora: " + self.engordadora + "Inversion: " + self.inversion + "Descripcion: " + self.descripcion + "Total: " + self.total
       return fila

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    