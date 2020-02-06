from django.urls import path

from index import views

urlpatterns = [
    path('gerar_banco', views.gerar_banco, name='gerar_banco'),
    path('limparBanco', views.limparBanco, name='limparBanco'),
    path('limparCertificado', views.limparCertificado, name='limparCertificado'),
    path('', views.index, name='index'),
]