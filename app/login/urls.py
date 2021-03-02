
from django.urls import path

from app.login.views import Inicio, Registrar, LogoutView, Acceder

app_name='login'

urlpatterns = [
    path('', Inicio.as_view(), name='inicio'),
    path('registrar/', Registrar.as_view(), name='registrar'),
    path('login/', Acceder.as_view(), name='login'),
    path('salir/', LogoutView.as_view(next_page='login:login'), name='salir'),
]
