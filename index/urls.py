from django.urls import path

from index import views

urlpatterns = [
    path('gerar_banco', views.gerar_banco, name='gerar_banco'),
    path('', views.index, name='index'),
]