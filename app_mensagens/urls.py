from django.urls import path
from . import views

urlpatterns = [
    # Exemplo de rota:
    path('', views.inbox, name='inbox'),
    # Outras rotas para o app de mensagens
]