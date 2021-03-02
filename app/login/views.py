from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.views import View



class Inicio(View):

    def get(self, request):
        template = 'inicio.html'
        return render(request, template)


class Registrar(View):

    def get(self, request):
        form = UserCreationForm
        template_name = 'registrar.html'
        forms = dict(form=form)
        return render(request, template_name, forms)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f'Bienvenid@ a la plataforma {nombre_usuario}')
            login(request, usuario)
            return redirect('login:inicio')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, 'registrar.html', {'form':form})

class Acceder(LoginView):
    template_name = 'acceder.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesion'
        return context


# def salir(request):
#     logout(request)
#     messages.success(request, 'Tu sesion se ha cerrado correctamente')
#     return redirect('login')
