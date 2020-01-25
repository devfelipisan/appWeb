from django import forms
from .models import *

class forms_curso(forms.ModelForm):
    class Meta:
        model = cadastroCurso
        fields = [
            "nome_curso",
            "validade_curso",
            "norma_curso",
            "carga_hora_curso"
        ]