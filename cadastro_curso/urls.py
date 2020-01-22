from django.urls import path
from cadastro_curso import views

urlpatterns = [
    path('cadastro/', views.cadastro_curso, name='cadastro_curso'),
]
