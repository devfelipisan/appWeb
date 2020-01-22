from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import cadastroUnidades
from .forms import forms_unidade
from cadastro_curso.models import cadastroCurso

mensagemcadastroexistente = "<div style='margin: auto; width: 50%; padding: 10px;'><p><h1 style='color:#B00020;'>Já existe um cadastro com esses dados</h1></p><br><input type='button' value='Voltar a página de cadastro' onclick='history.go(-1)'></div>"

def info_unidade(request, id):
    context={
    "information":cadastroUnidades.objects.get(id=id),
    "lista_cursos":cadastroUnidades.objects.get(id=id).cursos_necesarios.all(),
    }
    return render(request, "cadastrounidade/info_unidade.html", context)

    @deletar_cadastro
    def deletar_cadastro(id):
        deletar = unidadesCadastrada.objects.get(id=id)
        deletar.delete()
        print('Deletado')

        return HttpResponseRedirect('/unidade/cadastro')
    
    @alterar_cadastro
    def alterar_cadastro(id, valor):
        alterar = unidadesCadastrada.objects.get(id=id)
        print("Alterado")
        
        return HttpResponseRedirect('/unidade/cadastro')

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
                        new_unidade.cursosObrigatorios.add(cadastroCurso.objects.get(id=id))
                        new_unidade.save()

                    print(f"Unidade Cadastrada")

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


def frente_unidade_programada(request):
    return render(request, "cadastrounidade/frente_unidade_programada.html")