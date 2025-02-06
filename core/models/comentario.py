from django.db import models

from .user import User 
from .livro import Livro

class Comentario(models.Model):
    class Avaliacao(models.IntegerChoices):
        EXCELENTE = 5, "Excelente"
        BOM = 4, "Bom"
        REGULAR = 3, "Regular"
        RUIM = 2, "Ruim"
        PESSIMO = 1, "Pessimo"

    
    
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="usuario")
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name="livro",null=True, blank=False)
    data = models.DateTimeField(auto_now_add=True)
    nota = models.IntegerField(choices=Avaliacao.choices, default= Avaliacao.REGULAR)
    comentario = models.TextField(max_length=1000)


    def __str__(self):
        return f" Comentario do livro {self.livro} | {self.usuario}"

