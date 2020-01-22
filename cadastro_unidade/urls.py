from django.urls import path
from cadastro_unidade import views

urlpatterns = [
    path('info/<int:id>', views.info_unidade, name='info_unidade'),
    path('cadastro/', views.cadastro_unidade, name='cadastro_unidade'),
    path('frente_programada/', views.frente_unidade_programada, name='frente_unidade_programada'),
]
