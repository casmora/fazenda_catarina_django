from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao



class Regiao(models.Model):
    class Meta:
        verbose_name_plural = "regioes"
    nome_cidade = models.CharField(max_length=255)
    nome_estado = models.CharField(max_length=255)

    def __str__(self):
        return self.nome_cidade

class Produtor(models.Model):
    class Meta:
        verbose_name_plural = "produtores"

    nome =  models.CharField(max_length=255)
    nome_fazenda = models.CharField(max_length=255)

    def __str__(self):
        return self.nome, self.nome_fazenda

class Produto(models.Model):
    descricao = models.CharField(max_length=255)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="produtos")
    regiao =  models.ForeignKey(Regiao, on_delete=models.PROTECT, related_name="produtos")
    produtores = models.ManyToManyField(Produtor, related_name="produtos")

    def __str__(self):
        return "%s (%s)" %(self.descricao, self.regiao)


class Compra(models.Model):

    class StatusCompra(models.IntegerChoices):
        CARRINHO = 1, 'Carrinho'
        REALIZADO = 2, 'Realizado'
        PAGO = 3, 'Pago'
        ENTREGUE = 4, 'Entregue'

    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")  
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.CARRINHO) 

class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name= "+")
    quantidade = models.IntegerField()     
    

    




