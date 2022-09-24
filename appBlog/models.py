from datetime import datetime
import email
from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)

    def __str__(self):
        return f'{self.title} ({self.date})'

class Comment(models.Model):
    # Si no define el atributo de related_name, Django usará el nombre del modelo en minúsculas, seguido de _set (es decir, comment_set) para nombrar la relación del objeto relacionado con el objeto del modelo, donde esta relación ha sido definido.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    nombre = models.CharField(max_length=80, verbose_name='Nombre')
    correo = models.EmailField()
    comentario = models.TextField()
    # ordenar los comentarios en orden cronológico de forma predeterminada
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comentario de {self.nombre} en {self.post}'