from django import forms
from .models import *


class forms_unidade(forms.ModelForm):
    class Meta:
        model = cadastroUnidades
        fields = [
            "nome_unidade", "cursos_necesarios"
        ]
    
class forms_frente_programada(forms.ModelForm):
    class Meta:
        model = frenteProgramada
        fields = [
            "local_embarque",
            "data_ini_unidade",
            "local_desembarque",
            "data_fim_unidade",
            "sup_frente",
            "op_guincho_frente",
            "op_oxcorte_frente",
            "rigger_a_frente",
            "rigger_b_frente",
        ]