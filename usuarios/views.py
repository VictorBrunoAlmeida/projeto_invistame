from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.


def novo_usuario(request):
    #tipo da requisição, validar, informar e salvar no banco de dados
    
    if request.method =="POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #INFORMAR O USUÁRIO
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f"O usuario {usuario} foi criado com sucesso!")
            return redirect("login")
            #salvar o usuário no banco de dados
    else:
        formulario = UserRegisterForm()
    
        
    return render(request, "usuarios/registrar_usuario.html", {"formulario": formulario})

