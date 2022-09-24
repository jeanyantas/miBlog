from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'post', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('nombre', 'correo', 'comentario')