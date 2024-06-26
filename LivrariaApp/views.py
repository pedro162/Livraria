from django.forms import ModelForm
from .models import *
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['autor','editora','isbn','numeroPaginas','titulo','anoPublicacao','emailEditora']

#Última aula: https://www.devmedia.com.br/view/viewaula.php?idcomp=38005
#Last time: 3.57
def livro_list(request, template_name='livro_list.html'):
    livro = Livro.objects.all()
    livros = {'lista': livro}
    return render(request, template_name, livros)

def livro_new(request ,template_name='livro_form.html'):
    form = LivroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_livros')
    return render(request, template_name, {'form':form})

def livro_edit(request, pk, template_name='livro_form.html'):
   
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            livro = form.save()
            return redirect("listar_livros")
    else:
        form = LivroForm(instance=livro)
    return render(request, template_name, {'form':form})

def livro_delete(request, pk, template_name='livro_delete.html'):
   
    livro = Livro.objects.get(pk=pk)
    if request.method == 'POST':
        livro = livro.delete()
        return redirect("listar_livros")
    
    return render(request, template_name, {'livro':livro})


    