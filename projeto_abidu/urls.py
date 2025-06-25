"""
URL configuration for projeto_abidu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invistame import views
from usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import render, redirect


from django.contrib.auth import logout
from django.shortcuts import render, redirect


def custom_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'usuarios/logout.html')
    elif request.method == 'GET':
        logout(request)
        return render(request, 'usuarios/logout.html')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.investimentos, name="investimentos"),
    # path("contato/", views.contato),
    # path("minha_historia/", views.minha_historia, name="minha_historia"),
    path("novo_investimento/", views.criar, name="novo_investimento"),
    path("novo_investimento/<int:id_investimento>", views.editar, name="editar"),
    path("excluir_investimento/<int:id_investimento>",
         views.excluir, name="excluir"),
    # path("investimento_registrado/", views.investimento_registrado,
    #      name="investimento_registrado"),
    path("<int:id_investimento>/", views.detalhe, name="detalhe"),
    path("conta/",usuarios_views.novo_usuario, name="novo_usuario"),
    path("login/", auth_views.LoginView.as_view(template_name="usuarios/login.html"), name='login'),
    path('logout/', custom_logout_view, name='logout'),


]
