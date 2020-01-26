from django.urls import path
from cadastro_unidade import views

urlpatterns = [
    path('alterar/<int:id>', views.alterar_unidade, name='alterar_unidade'),
    path('deletar/<int:id>', views.deletar_unidade, name='deletar_unidade'),
    path('info/<int:id>', views.visualizar_unidade, name='visualizar_unidade'),
    path('cadastro/', views.cadastro_unidade, name='cadastro_unidade'),
    path('deletar_programacao/<int:id>', views.deletar_frente_programada, name='deletar_programacao'),
    path('alterar_programacao/<int:id>', views.alterar_frente_programada, name='alterar_programacao'),
    path('visualizar_programacao/<int:id>', views.visualizar_frente_programada, name='visualizar_programacao'),
    path('programar_frente/', views.programar_frente, name='programar_frente'),
]
