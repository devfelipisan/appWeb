from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import cadastroUnidades
from .forms import forms_unidade
from cadastro_curso.models import cadastroCurso

mensagemcadastroexistente = "<div style='margin: auto; width: 50%; padding: 10px;'><p><h1 style='color:#B00020;'>Já existe um cadastro com esses dados</h1></p><br><input type='button' value='Voltar a página de cadastro' onclick='history.go(-1)'></div>"

def cadastro_unidade(request, *args):
    form_cadastro_unidade = forms_unidade(request.POST)
    if request.method == "POST":
        if form_cadastro_unidade.is_valid():
            nomeUnidade = form_cadastro_unidade.cleaned_data['nomeUnidade']
            cursosObrigatorios = form_cadastro_unidade.cleaned_data['cursosObrigatorios']

            try:
                if not bool(cadastroUnidades.objects.filter(nome_unidade=nomeUnidade)):
                    new_unidade = cadastroUnidades(nome_unidade=nomeUnidade.upper())
                    new_unidade.save()
                    for id in cursosObrigatorios:
                        new_unidade.cursos_necesarios.add(cadastroCurso.objects.get(id=id))
                        new_unidade.save()

                    return HttpResponseRedirect('/unidade/cadastro')
                    
                else:
                    return HttpResponse(mensagemcadastroexistente)
            
            except Exception as error:
                print(error)
                return HttpResponseRedirect('/unidade/cadastro')

        else:
            return HttpResponseRedirect('/unidade/cadastro')

        return HttpResponseRedirect('/unidade/cadastro')
    
    context = {
        'form_cadastro_unidade': form_cadastro_unidade,
        'lista_unidades_cadastradas': cadastroUnidades.objects.all(),
    }

    return render(request, "cadastrounidade/cadastro_unidades.html", context)    

def infor_unidade(function):
    def new_function(*args, **kwargs):
        return function(*args, **kwargs)

    return new_function

@infor_unidade
def deletar_unidade(request, id):
    deletar = cadastroUnidades.objects.get(id=id)
    deletar.delete()
    return HttpResponseRedirect('/unidade/cadastro')

@infor_unidade
def alterar_unidade(request, id, *args):
    alterar = cadastroUnidades.objects.get(id=id)
    form_cadastro_unidade = forms_unidade(request.POST)
    if request.method == "POST":
        #Deixei este if como not por não estarmos utilizando todos os campos do formulário nesta view
        if not form_cadastro_unidade.is_valid():
            cursosObrigatorios = form_cadastro_unidade.cleaned_data['cursosObrigatorios']
            alterar = cadastroUnidades.objects.get(id=id)
            alterar.cursos_necesarios.clear()
            for id in cursosObrigatorios:
                alterar.cursos_necesarios.add(cadastroCurso.objects.get(id=id))
                alterar.save()
        
    return HttpResponseRedirect('/unidade/cadastro')

@infor_unidade
def visualizar_unidade(request, id):
    form_cadastro_unidade = forms_unidade(request.POST)

    context={
        'form_cadastro_unidade': form_cadastro_unidade,
        "information":cadastroUnidades.objects.get(id=id),
        "lista_cursos":cadastroUnidades.objects.get(id=id).cursos_necesarios.all(),
    }
    return render(request, "cadastrounidade/info_unidade.html", context)

def frente_unidade_programada(request):
    return render(request, "cadastrounidade/frente_unidade_programada.html")