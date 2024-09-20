from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=5000)
    imagem = models.ImageField(blank=True, upload_to='media/')
    
    def __str__(self):
        return self.titulo
    
# tem que ter 2 models e relação entre eles