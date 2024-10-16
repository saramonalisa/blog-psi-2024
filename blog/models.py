from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=5000)
    imagem = models.ImageField(blank=True)
    
    def __str__(self):
        return self.titulo