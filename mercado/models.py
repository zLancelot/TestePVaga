from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Produto(models.Model):
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'produto'


class Venda(models.Model):
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_produto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='id_produto', blank=True, null=True)
    data_venda = models.DateField(blank=True, null=True)
    id_vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, db_column='id_vendedor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venda'


class Vendedor(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    login = models.CharField(max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'
