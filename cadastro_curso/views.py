from django.shortcuts import render

def cadastro_curso(request):
    return render(request, "cadastrocurso/cadastro_curso.html")