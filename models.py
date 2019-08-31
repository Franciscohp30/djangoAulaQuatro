from django.db import models


class TipoVeiculo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'TipoVeiculo'


class Veiculos(models.Model):
    placa = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=20)
    ano = models.CharField(max_length=10)
    km = models.CharField(max_length=50)
    tipo = models.ForeignKey( TipoVeiculo , on_delete=models.CASCADE)
    obs = models.TextField( blank=True , null=True )
    foto = models.ImageField( blank=True , null=True )


    def __str__(self):
        return self.placa

    class Meta:
        verbose_name_plural = 'Veículos'

