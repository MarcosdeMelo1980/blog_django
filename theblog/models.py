# Importa o módulo models do Django, que contém a classe base para todos os modelos
from django.db import models
# Importa o modelo User do módulo de autenticação do Django, que é usado para representar usuários. Esse foi o usuário que você criou no painel. 
from django.contrib.auth.models import User
from django.urls import reverse

# Defina os seus modelos aqui.
class Post(models.Model):
    # Campo de texto para o título do post, com um comprimento máximo de 255 caracteres
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Blog Post')
    
    
    # Campo que estabelece uma relação de chave estrangeira com o modelo User,
    # indicando que cada post é escrito por um único usuário (autor)
    # A opção on_delete=models.CASCADE indica que, se o usuário for deletado,
    # todos os posts associados a ele também serão deletados.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    
    
    # Método mágico para retornar uma representação em string do objeto Post
    def __str__(self):
    # Retorna o título do post junto com o nome de usuário do autor
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse('article-details', args=[str(self.id)])
