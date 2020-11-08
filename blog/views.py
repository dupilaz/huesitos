from django.shortcuts import render
from django.utils import timezone
from .models import Servicio
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.


def prueba(request):
    
    return render(request, 'blog/prueba.html')

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, 'blog/servicio.html', {"servicios":servicios})    
def contacto(request):
    form = PostForm()
    return render(request, 'blog/contacto.html', {'form': form})
        


   
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/contacto.html', {'form': form})
