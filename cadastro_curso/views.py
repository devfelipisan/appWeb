from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import forms_curso
from .models import cadastroCurso

mensagemcadastroexistente = "<div style='margin: auto; width: 50%; padding: 10px;'><p><h1 style='color:#B00020;'>Já existe um cadastro com esses dados</h1></p><br><input type='button' value='Voltar a página de cadastro' onclick='history.go(-1)'></div>"

def cadastro_curso(request):
    form_cadastro_curso = forms_curso(request.POST)
    if request.method == "POST":
        print('Formulário requisitado como POST')
        if form_cadastro_curso.is_valid():
            print('Formulário validado')
            nome_curso = form_cadastro_curso.cleaned_data[
                'nome_curso'
            ]
            validade_curso = form_cadastro_curso.cleaned_data[
                'validade_curso'
            ]
            norma_curso = form_cadastro_curso.cleaned_data[
                'norma_curso'
            ]
            carga_hora_curso = form_cadastro_curso.cleaned_data[
                'carga_hora_curso'
            ]

            try:
                if not bool(
                    cadastroCurso.objects.filter(
                        nome_curso = nome_curso,
                    )
                ):
                    new_curso = cadastroCurso(
                        nome_curso = nome_curso,
                        validade_curso = validade_curso,
                        norma_curso = norma_curso,
                        carga_hora_curso = carga_hora_curso,
                    )
                    new_curso.save()

                    return HttpResponseRedirect(
                        '/curso/cadastro'
                    )
                
                else:
                    return HttpResponse(
                        mensagemcadastroexistente
                    )
            
            except Exception as error:
                print(error)
                return HttpResponseRedirect(
                    '/curso/cadastro'
                )
                
        else:
            print(
                'Formulário não validado'
            )

            return HttpResponseRedirect(
                '/curso/cadastro'
            )
        
    context = {
        'form_cadastro_curso': form_cadastro_curso,
        'lista_cursos_cadastrado': cadastroCurso.objects.all(),
    }

    return render(request, "cadastrocurso/cadastro_curso.html", context)


def infor_cursos(function):
    def new_function(*args, **kwargs):
        return function(*args, **kwargs)

    return new_function

@infor_cursos
def deletar_curso(request,id):
    deletar = cadastroCurso.objects.get(
        id=id
    )
    
    deletar.delete()
    return HttpResponseRedirect(
        '/curso/cadastro'
    )

@infor_cursos
def alterar_curso(request, id, *args):
    alterar = cadastroCurso.objects.get(id=id)
    form_cadastro_curso = forms_curso(request.POST)
    
    if request.method == "POST":
        print('Formulário requisitado como POST')
         
        #Deixei este if como not por não estarmos utilizando todos os campos 
        #do formulário nesta view
        if form_cadastro_curso.is_valid():
            print('Formulário validado')
            nome_curso = form_cadastro_curso.cleaned_data['nome_curso']
            validade_curso = form_cadastro_curso.cleaned_data['validade_curso']
            norma_curso = form_cadastro_curso.cleaned_data['norma_curso']
            carga_hora_curso = form_cadastro_curso.cleaned_data['carga_hora_curso']
                      
            alterar = cadastroCurso.objects.get(id=id)
            if bool(nome_curso):
                alterar.nome_curso = nome_curso
            else:
                alterar.nome_curso = alterar.nome_curso
            
            if bool(validade_curso):
                alterar.validade_curso = validade_curso
            else:
                alterar.validade_curso = alterar.validade_curso
            
            if bool(norma_curso):
                alterar.norma_curso = norma_curso
            else:
                alterar.norma_curso = alterar.norma_curso
            
            if bool(carga_hora_curso):
                alterar.carga_hora_curso = carga_hora_curso
            else:
                alterar.carga_hora_curso = alterar.carga_hora_curso
            
            alterar.save()
        
    return HttpResponseRedirect('/curso/cadastro')

@infor_cursos
def visualizar_curso(request, id):
    form_cadastro_curso = forms_curso(
        request.POST
    )

    context={
        'form_cadastro_curso': form_cadastro_curso,
        "information":cadastroCurso.objects.get(
            id=id
        )
    }
    return render(
        request,
        "cadastrocurso/info_curso.html",
        context
    )