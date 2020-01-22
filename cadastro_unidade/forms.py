from django import forms
from cadastro_curso.models import cadastroCurso


class forms_unidade(forms.Form):
    nomeUnidade = forms.CharField(help_text='Insira o nome da unidade que será atendida',
                                  label='Nome da Unidade', max_length=64,
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'Informe o nome da nova unidade',
                                      'aria-label': 'Nome da unidade'}))
    
    lista = cadastroCurso.objects.all()
    choiceList = []
    for item in lista:
        choiceList.append((item.id,item))

    cursosObrigatorios = forms.MultipleChoiceField(choices=choiceList,
        help_text='Selecione os cursos obrigatórios para esta unidade',
        label='Selecione os cursos obrigatórios',widget=forms.SelectMultiple(attrs={
            'class':'form-control',
            'multiple':'multiple'
        }))