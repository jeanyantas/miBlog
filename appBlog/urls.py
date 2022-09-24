from django.urls import path
from .views import posts, post_detail, formulario, publicar, about

app_name = 'miBlog'

urlpatterns = [
    path('', posts, name="posts"),
    path('<int:post_id>', post_detail, name="post_detail"),
    path('formulario/', formulario, name="formulario"),
    path('publicar/', publicar, name="publicar"),
    path('about/', about, name="about"),
]