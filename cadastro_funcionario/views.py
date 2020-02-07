from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import forms_funcionario, forms_certificado_funcionario
from .models import cadastroFuncionario, certificadoFuncionario
from cadastro_unidade.models import frenteProgramada

mensagemcadastroexistente = "<div style='margin: auto; width: 50%; padding: 10px;'><p><h1 style='color:#B00020;'>Já existe um cadastro com esses dados</h1></p><br><input type='button' value='Voltar a página de cadastro' onclick='history.go(-1)'></div>"

def cadastro_funcionario(request):
    form_cadastro_funcionario = forms_funcionario(request.POST)
    if request.method == "POST":
        print('formulário requisitado como POST')
        if form_cadastro_funcionario.is_valid():
            print('Formulário validado')
            matricula_funcionario = form_cadastro_funcionario.cleaned_data[
                'matricula_funcionario'
            ]
            nome_completo_funcionario = form_cadastro_funcionario.cleaned_data[
                'nome_completo_funcionario'
            ]
            funcao_funcionario = form_cadastro_funcionario.cleaned_data[
                'funcao_funcionario'
            ]
            cpf_funcionario = form_cadastro_funcionario.cleaned_data[
                'cpf_funcionario'
            ]
            sispat_funcionario = form_cadastro_funcionario.cleaned_data[
                'sispat_funcionario'
            ]
            
            try:
                if not bool(
                    cadastroFuncionario.objects.filter(
                        matricula_funcionario=matricula_funcionario
                    )
                ):

                    new_employee = cadastroFuncionario(
                        matricula_funcionario = matricula_funcionario,
                        nome_completo_funcionario = nome_completo_funcionario,
                        funcao_funcionario = funcao_funcionario,
                        cpf_funcionario = cpf_funcionario,
                        sispat_funcionario = sispat_funcionario,
                        disponibilidade_funcionario = True,
                    )
                    new_employee.save()

                    return HttpResponseRedirect(
                        '/funcionario/cadastro'
                    )
                   
                else:
                    return HttpResponse(
                        mensagemcadastroexistente
                    )
            
            except Exception as error:
                print(error)
                return HttpResponseRedirect(
                    '/funcionario/cadastro'
                )

        else:
            print(
                'Formulário não validado'
            )
            
            return HttpResponseRedirect(
                '/funcionario/cadastro'
            )

        return HttpResponseRedirect(
            '/funcionario/cadastro'
        )
    matricula = cadastroFuncionario.objects.all()
    for i in range(1,len(matricula)-1):
        if frenteProgramada.objects.filter(
            sup_frente=matricula[i].matricula_funcionario
            ) or frenteProgramada.objects.filter(
                op_guincho_frente=matricula[i].matricula_funcionario
                ) or frenteProgramada.objects.filter(
                    op_oxcorte_frente=matricula[i].matricula_funcionario
                    ) or frenteProgramada.objects.filter(
                        rigger_a_frente=matricula[i].matricula_funcionario
                        ) or frenteProgramada.objects.filter(
                            rigger_b_frente=matricula[i].matricula_funcionario):
            tornarDisponivel = cadastroFuncionario.objects.get(matricula_funcionario=matricula[i].matricula_funcionario)
            tornarDisponivel.disponibilidade_funcionario = False
            tornarDisponivel.save()
                            
        else:
            tornarDisponivel = cadastroFuncionario.objects.get(matricula_funcionario=matricula[i].matricula_funcionario)
            tornarDisponivel.disponibilidade_funcionario = True
            tornarDisponivel.save()

    context = {
        'form_cadastro_funcionario': form_cadastro_funcionario,
        'lista_funcionarios_cadastrados': cadastroFuncionario.objects.all(),
    }
    
    return render(
        request,
        "cadastrofuncionario/cadastro_funcionario.html",
        context
    )

def infor_funcionario(function):
    def new_function(*args, **kwargs):
        return function(*args, **kwargs)

    return new_function

@infor_funcionario
def deletar_funcionario(request,id):
    deletar = cadastroFuncionario.objects.get(
        matricula_funcionario=id
    )
    
    deletar.delete()
    return HttpResponseRedirect(
        '/funcionario/cadastro'
    )

@infor_funcionario
def alterar_funcionario(request, id, *args):
    alterar = cadastroFuncionario.objects.get(
        matricula_funcionario=id
    )
    
    form_cadastro_funcionario = forms_funcionario(
        request.POST
    )
    
    if request.method == "POST":
        #Deixei este if como not por não estarmos utilizando todos os campos 
        #do formulário nesta view
        if not form_cadastro_funcionario.is_valid():
            nome_completo_funcionario = form_cadastro_funcionario.cleaned_data[
                'nome_completo_funcionario'
            ]
            funcao_funcionario = form_cadastro_funcionario.cleaned_data[
                'funcao_funcionario'
            ]
            cpf_funcionario = form_cadastro_funcionario.cleaned_data[
                'cpf_funcionario'
            ]
            sispat_funcionario = form_cadastro_funcionario.cleaned_data[
                'sispat_funcionario'
            ]
            
            alterar = cadastroFuncionario.objects.get(
                matricula_funcionario=id
            )
            if nome_completo_funcionario:
                alterar.nome_completo_funcionario = nome_completo_funcionario
            else:
                alterar.nome_completo_funcionario = alterar.nome_completo_funcionario
            
            if funcao_funcionario:
                alterar.funcao_funcionario = funcao_funcionario
            else:
                alterar.funcao_funcionario = alterar.funcao_funcionario
            
            if cpf_funcionario:
                alterar.cpf_funcionario = cpf_funcionario
            else:
                alterar.cpf_funcionario = alterar.cpf_funcionario
            
            if sispat_funcionario:
                alterar.sispat_funcionario = sispat_funcionario
            else:
                alterar.sispat_funcionario = alterar.sispat_funcionario
            
            alterar.save()
        
    return HttpResponseRedirect(
        '/funcionario/cadastro'
    )

@infor_funcionario
def visualizar_funcionario(request, id):
    form_cadastro_funcionario = forms_funcionario(
        request.POST
    )
    #sup_frente
    #op_guincho_frente
    #op_oxcorte_frente
    #rigger_a_frente
    #rigger_b_frente

    context={
        #'embarque':frenteProgramada.objects.filter(cadastroFuncionario.objects.get(matricula_funcionario=id).nome_completo_funcionario__in=frenteProgramada.objects.all()),
        "form_cadastro_funcionario": form_cadastro_funcionario,
        "information":cadastroFuncionario.objects.get(matricula_funcionario=id),
        "lista_cursos_ativos":certificadoFuncionario.objects.filter(nome_funcionario = id).all()
    }
    return render(
        request,
        "cadastrofuncionario/info_funcionario.html",
        context
    )

def certificado_funcionario(request):

    forms_certificado = forms_certificado_funcionario(request.POST)
    
    if request.method == "POST":
        print('formulário requisitado como POST')
        
        if forms_certificado.is_valid():
            print('Formulário validado')
            nome_funcionario = forms_certificado.cleaned_data[
                'nome_funcionario'
            ]
            curso_funcionario = forms_certificado.cleaned_data[
                'curso_funcionario'
            ]
            data_realizada = forms_certificado.cleaned_data[
                'data_realizada'
            ]
            valido_ate = forms_certificado.cleaned_data[
                'valido_ate'
            ]
            
            try:
                new_certified = certificadoFuncionario(
                    nome_funcionario = nome_funcionario,
                    curso_funcionario = curso_funcionario,
                    data_realizada = data_realizada,
                    valido_ate = valido_ate
                )
                new_certified.save()

                return HttpResponseRedirect(
                    '/funcionario/certificado'
                )
                            
            except Exception as error:
                print(error)
                return HttpResponseRedirect(
                    '/funcionario/certificado'
                )

        else:
            print(
                'Formulário não validado'
            )
            
            return HttpResponseRedirect(
                '/funcionario/certificado'
            )

        return HttpResponseRedirect(
            '/funcionario/certificado'
        )

    context = {
        'forms_certificado': forms_certificado,
    }
    
    return render(
        request,
        "cadastrofuncionario/certificado_funcionario.html",
        context
    )
