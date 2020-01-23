from django.urls import path
from cadastro_unidade import views

urlpatterns = [
    path('alterar/<int:id>', views.alterar_unidade, name='alterar_unidade'),
    path('deletar/<int:id>', views.deletar_unidade, name='deletar_unidade'),
    path('info/<int:id>', views.visualizar_unidade, name='visualizar_unidade'),
    path('cadastro/', views.cadastro_unidade, name='cadastro_unidade'),
    path('frente_programada/', views.frente_unidade_programada, name='frente_unidade_programada'),
]
