from django.db import models

class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    tecnologias = models.CharField(max_length=200, help_text="Ex: Python, Django, Tailwind")
    link_github = models.URLField(blank=True, null=True)
    link_deploy = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

# Create your models here.
