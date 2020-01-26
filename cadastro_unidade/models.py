from django.db import models
from cadastro_curso.models import cadastroCurso
from cadastro_funcionario.models import cadastroFuncionario
from datetime import datetime

class cadastroUnidades(models.Model):
    #Campo para nome da nova unidade
    nome_unidade = models.CharField(max_length=64)
    #Campo destinado para selecionar os cursos obrigatórios.
    cursos_necesarios = models.ManyToManyField(cadastroCurso)

    def __str__(self):
        return f"{str(self.nome_unidade).upper()}"

#programação da frente para a unidade cadastrada
class frenteProgramada(models.Model):
    #Nome da unidade programada
    nome_unidade = models.ForeignKey(cadastroUnidades, on_delete=models.CASCADE, related_name='nome_da_unidade')
    #Campos para embarque
    local_embarque = models.CharField(max_length=64)
    data_ini_unidade = models.DateField()
    #Campos para desembarque
    local_desembarque = models.CharField(max_length=64)
    data_fim_unidade = models.DateField()
    #Equipe programada
    sup_frente = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE, related_name='nome_do_supervisor')
    op_guincho_frente = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE, related_name='nome_do_opGuincho')
    op_oxcorte_frente = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE, related_name='nome_do_opOxCorte')
    rigger_a_frente = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE, related_name='nome_do_1_rigger')
    rigger_b_frente = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE, related_name='nome_do_2_rigger')

    def __str__(self):
        return f"Unidade {self.nome_unidade} - {self.data_ini_unidade}"