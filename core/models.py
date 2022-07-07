<<<<<<< HEAD
from statistics import mode
=======
>>>>>>> a50de280d4c99ccbf43242a4e474e6463d76a91e
from tabnanny import verbose
from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField()

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Autores"


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=32)
    quantidade = models.IntegerField()
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(
<<<<<<< HEAD
        Categoria, on_delete=models.PROTECT, related_name='livros')
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name='livros')
=======
        Categoria, on_delete=models.PROTECT, related_name="livros"
    )
    editora = models.ForeignKey(
        Editora, on_delete=models.PROTECT, related_name="livros"
    )
>>>>>>> a50de280d4c99ccbf43242a4e474e6463d76a91e

    def __str__(self):
        return f'{self.titulo} ({self.quantidade})'
