from django import forms
from .models import *


class forms_unidade(forms.ModelForm):
    class Meta:
        model = cadastroUnidades
        fields = [
            "nome_unidade", "cursos_necesarios"
        ]