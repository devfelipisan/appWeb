from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import cadastroUnidades, frenteProgramada
from .forms import forms_unidade, forms_frente_programada
from cadastro_curso.models import cadastroCurso
from cadastro_funcionario.models import cadastroFuncionario

mensagemcadastroexistente = "<div style='margin: auto; width: 50%; padding: 10px;'><p><h1 style='color:#B00020;'>Já existe um cadastro com esses dados</h1></p><br><input type='button' value='Voltar a página de cadastro' onclick='history.go(-1)'></div>"

def cadastro_unidade(request, *args):
    form_cadastro_unidade = forms_unidade(request.POST)
    if request.method == "POST":
        print('Unidade recebeu um methodo POST')
        if form_cadastro_unidade.is_valid():
            print('Formulário recebido é válido')
            nome_unidade = form_cadastro_unidade.cleaned_data['nome_unidade']
            cursos_necesarios = form_cadastro_unidade.cleaned_data['cursos_necesarios']

            try:
                if not bool(cadastroUnidades.objects.filter(nome_unidade=nome_unidade)):
                    new_unidade = cadastroUnidades(nome_unidade=nome_unidade)
                    new_unidade.save()
                    print('unidade cadastrada!')
                    for id in cursos_necesarios:
                        new_unidade.cursos_necesarios.set(cursos_necesarios)
                        new_unidade.save()

                    return HttpResponseRedirect('/unidade/cadastro')
                    
                else:
                    print('Já existe essa informação')
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
            cursos_necesarios = form_cadastro_unidade.cleaned_data['cursos_necesarios']
            alterar = cadastroUnidades.objects.get(id=id)
            alterar.cursos_necesarios.clear()
            for id in cursos_necesarios:
                alterar.cursos_necesarios.set(cursos_necesarios)
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

def programar_frente(request):
    form_cadastro_programar_frente = forms_frente_programada(request.POST)
    if request.method == "POST":
        print("Frente Programada recebeu o formulário no método POST")
        if form_cadastro_programar_frente.is_valid():
            print('Formulário validado com sucesso')
            nome_unidade = form_cadastro_programar_frente.cleaned_data['nome_unidade']
            local_embarque = form_cadastro_programar_frente.cleaned_data['local_embarque']
            data_ini_unidade = form_cadastro_programar_frente.cleaned_data['data_ini_unidade']
            local_desembarque = form_cadastro_programar_frente.cleaned_data['local_desembarque']
            data_fim_unidade = form_cadastro_programar_frente.cleaned_data['data_fim_unidade']
            sup_frente = form_cadastro_programar_frente.cleaned_data['sup_frente']
            op_guincho_frente = form_cadastro_programar_frente.cleaned_data['op_guincho_frente']
            op_oxcorte_frente = form_cadastro_programar_frente.cleaned_data['op_oxcorte_frente']
            rigger_a_frente = form_cadastro_programar_frente.cleaned_data['rigger_a_frente']
            rigger_b_frente = form_cadastro_programar_frente.cleaned_data['rigger_b_frente']
            
            funcionario_selecionado = [
                sup_frente,
                op_guincho_frente,
                op_oxcorte_frente,
                rigger_a_frente,
                rigger_b_frente,
            ]

            for funcionario in funcionario_selecionado:
                alterar_status = cadastroFuncionario.objects.get(matricula_funcionario=funcionario.matricula_funcionario)
                alterar_status.disponibilidade_funcionario = False
                alterar_status.save()

            new_front = frenteProgramada(
                nome_unidade=nome_unidade,
                local_embarque=local_embarque,
                data_ini_unidade=data_ini_unidade,
                local_desembarque=local_desembarque,
                data_fim_unidade=data_fim_unidade,
                sup_frente=sup_frente,
                op_guincho_frente=op_guincho_frente,
                op_oxcorte_frente=op_oxcorte_frente,
                rigger_a_frente=rigger_a_frente,
                rigger_b_frente=rigger_b_frente,
            )
            new_front.save()     

            return HttpResponseRedirect('/unidade/programar_frente')
        
        else:
            return HttpResponseRedirect('/unidade/programar_frente')

    context = {
        'form_cadastro_programar_frente': form_cadastro_programar_frente,
        'lista_frentes_programadas': frenteProgramada.objects.all(),
    }
    #Filtra o contexto a ser exibido na view antes da renderização.
    context['form_cadastro_programar_frente'].fields['rigger_b_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='rigger').all()
    context['form_cadastro_programar_frente'].fields['rigger_a_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='rigger').all()
    context['form_cadastro_programar_frente'].fields['op_oxcorte_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='opOxCorte').all()
    context['form_cadastro_programar_frente'].fields['op_guincho_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='opGuincho').all()
    context['form_cadastro_programar_frente'].fields['sup_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='supervisor').all()
    
    return render(request, "cadastrounidade/frente_unidade_programada.html", context)

def infor_frente_programada(function):
    def new_function(*args, **kwargs):
        return function(*args, **kwargs)

    return new_function

@infor_frente_programada
def deletar_frente_programada(request, id):
    deletar = frenteProgramada.objects.get(id=id)
    print('Formulário sendo setado para deletar')
    deletar.delete()
    print('Formulário deletado')
    return HttpResponseRedirect('/unidade/programar_frente')

@infor_frente_programada
def alterar_frente_programada(request, id):
    
    form_cadastro_programar_frente = forms_frente_programada(request.POST)

    if request.method == "POST":
        print('Formulário recebido como POST')
        #Deixei este if como not por não estarmos utilizando todos os campos do formulário nesta view
        if not form_cadastro_programar_frente.is_valid():
            print('Formulário validado')
            nome_unidade = form_cadastro_programar_frente.cleaned_data['nome_unidade']
            local_embarque = form_cadastro_programar_frente.cleaned_data['local_embarque']
            data_ini_unidade = form_cadastro_programar_frente.cleaned_data['data_ini_unidade']
            local_desembarque = form_cadastro_programar_frente.cleaned_data['local_desembarque']
            data_fim_unidade = form_cadastro_programar_frente.cleaned_data['data_fim_unidade']
            sup_frente = form_cadastro_programar_frente.cleaned_data['sup_frente']
            op_guincho_frente = form_cadastro_programar_frente.cleaned_data['op_guincho_frente']
            op_oxcorte_frente = form_cadastro_programar_frente.cleaned_data['op_oxcorte_frente']
            rigger_a_frente = form_cadastro_programar_frente.cleaned_data['rigger_a_frente']
            rigger_b_frente = form_cadastro_programar_frente.cleaned_data['rigger_b_frente']

            funcionario_selecionado = [
                sup_frente,
                op_guincho_frente,
                op_oxcorte_frente,
                rigger_a_frente,
                rigger_b_frente,
            ]
            print('Formulário passando pela lista funcionario selecionado')

            for funcionario in funcionario_selecionado:
                alterar_status = cadastroFuncionario.objects.get(matricula_funcionario=frenteProgramada.objects.get(id=id).funcionario)
                alterar_status.disponibilidade_funcionario = True
                alterar_status.save()
            print('Formulário passou pelo loop de alteração de status dos funcionários')

            change_front = frenteProgramada(
                nome_unidade=nome_unidade,
                local_embarque=local_embarque,
                data_ini_unidade=data_ini_unidade,
                local_desembarque=local_desembarque,
                data_fim_unidade=data_fim_unidade,
                sup_frente=sup_frente,
                op_guincho_frente=op_guincho_frente,
                op_oxcorte_frente=op_oxcorte_frente,
                rigger_a_frente=rigger_a_frente,
                rigger_b_frente=rigger_b_frente,
            )
            change_front.save()
            print('Alterações salvas do formulário')
    
    return HttpResponseRedirect('/unidade/programar_frente')

@infor_frente_programada
def visualizar_frente_programada(request, id):
    form_cadastro_programar_frente = forms_frente_programada(request.POST)

    context={
        'form_cadastro_programar_frente': form_cadastro_programar_frente,
        "information":frenteProgramada.objects.get(id=id),
    }
     #Filtra o contexto a ser exibido na view antes da renderização.
    context['form_cadastro_programar_frente'].fields['rigger_b_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='rigger').all()
    context['form_cadastro_programar_frente'].fields['rigger_a_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='rigger').all()
    context['form_cadastro_programar_frente'].fields['op_oxcorte_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='opOxCorte').all()
    context['form_cadastro_programar_frente'].fields['op_guincho_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='opGuincho').all()
    context['form_cadastro_programar_frente'].fields['sup_frente'].queryset = cadastroFuncionario.objects.exclude(
        disponibilidade_funcionario=False).filter(funcao_funcionario='supervisor').all()
    return render(request, "cadastrounidade/infor_frente_programada.html", context)