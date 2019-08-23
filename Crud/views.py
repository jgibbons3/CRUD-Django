from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.forms import ModelForm
from django.contrib import messages
from django.core.paginator import Paginator

def usuarioList(request):
    data_list=Usuario.objects.all()
    paginator=Paginator(data_list, 7)

    page = request.GET.get('page')
    data = paginator.get_page(page)
    return render(request, 'Crud/listaUsuarios.html', {'data': data})

class PostsForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['name', 'apellido', 'edad', 'telefono', 'email', 'domicilio']

def usuarioCreate(request):
    form = PostsForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'New contact successfully created.')
        return redirect('index')
    return render(request, 'Crud/createUsuario.html', {'form': form})

def usuarioDelete(request, id):
    print (id)
    post = get_object_or_404(Usuario, id=id)
    post.delete()
    messages.add_message(request, messages.SUCCESS, 'Contact successfully deleted.')
    return redirect ('index')

def usuarioUpdate(request, id):
    post = get_object_or_404(Usuario, id=id)
    #return usuarioCreate
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Contact successfully updated.')
        return redirect('index')
    return render(request, 'Crud/createUsuario.html', {'form': form})
    


