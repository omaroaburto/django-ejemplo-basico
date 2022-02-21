from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.usuarioslist, name='usuario_list'),
]