from django.urls import path
from cadastro_funcionario import views

urlpatterns = [
    path('cadastro/', views.cadastro_funcionario, name='cadastro_funcionario'),
    path('certificado/', views.certificado_funcionario, name='certificado_funcionario'),
]
