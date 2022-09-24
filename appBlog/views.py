from django.shortcuts import get_object_or_404, render, redirect

from .models import Post, Comment
from .forms import CommentForm

# Paginador de Django
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def posts(request):
    posts = Post.objects.all()[::-1]

    # Paginador 
    paginator = Paginator(posts, 3) # 3 comentarios por página
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un número entero, entregue la primera página
        posts = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, entrega la última página de resultados
        posts = paginator.page(paginator.num_pages)

    context = {'posts': posts, 'page': page}
    return render(request, 'posts.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments =  post.comments.all()

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(request.path)
    else:
        # Creando instancia de CommentForm si la vista es llamada por una solicitud GET
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form}
    return render(request, 'post_detail.html', context)

def formulario(request):
    return render(request, 'formulario.html')

def publicar(request):
    if request.method == "POST":
        titulo = request.POST['txtTitulo']
        descripcion = request.POST['txtDescripcion']
        imagen = request.FILES['imagen']
        fecha = request.POST['txtFecha']
        publicacion = Post.objects.create(title=titulo,description=descripcion,image=imagen,date=fecha)
        return redirect('/')

def about(request):
    return render(request, 'about.html')