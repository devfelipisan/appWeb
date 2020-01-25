from django.urls import path
from cadastro_curso import views

urlpatterns = [
    path('alterar/<int:id>', views.alterar_curso, name='alterar_curso'),
    path('deletar/<int:id>', views.deletar_curso, name='deletar_curso'),
    path('info/<int:id>', views.visualizar_curso, name='visualizar_curso'),
    path('cadastro/', views.cadastro_curso, name='cadastro_curso'),
]
