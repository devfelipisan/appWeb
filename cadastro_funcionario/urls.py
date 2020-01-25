from django.urls import path
from cadastro_funcionario import views

urlpatterns = [
    path('alterar/<int:id>', views.alterar_funcionario, name='alterar_funcionario'),
    path('deletar/<int:id>', views.deletar_funcionario, name='deletar_funcionario'),
    path('info/<int:id>', views.visualizar_funcionario, name='visualizar_funcionario'),
    path('cadastro/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('certificado/', views.certificado_funcionario, name='certificado_funcionario'),
]
