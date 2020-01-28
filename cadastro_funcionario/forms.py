from django import forms
from .models import *

class forms_funcionario(forms.ModelForm):

    class Meta:
        model = cadastroFuncionario
        fields = [
            'matricula_funcionario',
            'nome_completo_funcionario',
            'funcao_funcionario',
            'cpf_funcionario',
            'sispat_funcionario',
            'disponibilidade_funcionario',
        ]

class forms_certificado_funcionario(forms.ModelForm):

    class Meta:
        model = certificadoFuncionario
        fields = [
            'nome_funcionario',
            'curso_funcionario',
            'data_realizada',
            'valido_ate',
        ]