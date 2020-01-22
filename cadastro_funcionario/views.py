from django.shortcuts import render

def cadastro_funcionario(request):
    return render(request, "cadastrofuncionario/cadastro_funcionario.html")

def certificado_funcionario(request):
    return render(request, "cadastrofuncionario/certificado_funcionario.html")