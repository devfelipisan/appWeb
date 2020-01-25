from django.db import models
from cadastro_curso.models import cadastroCurso

class cadastroFuncionario(models.Model):
    opcao_funcao = [
        ['supervisor','Supervisor'],
        ['opGuincho','Operador de Guincho'],
        ['opOxCorte','Operador de OxCorte'],
        ['rigger','Rigger']
    ]
    matricula_funcionario = models.IntegerField(primary_key=True)
    nome_completo_funcionario = models.CharField(max_length=64)
    funcao_funcionario = models.CharField(max_length=64, choices=opcao_funcao)
    cpf_funcionario = models.IntegerField()
    sispat_funcionario = models.IntegerField()
    disponibilidade_funcionario = models.BooleanField(default=True)
    
    def disponivel(disponibilidade_funcionario):
        if disponibilidade_funcionario:
            return f"Disponível para o embarque"
        else:
            return f"Não disponível para embarque"

    def __str__(self):
        return f"{self.nome_completo_funcionario}"

class certificadoFuncionario(models.Model):
    nome_funcionario = models.ForeignKey(cadastroFuncionario, on_delete=models.CASCADE)
    curso_funcionario = models.ForeignKey(cadastroCurso, on_delete=models.CASCADE)
    data_realizada = models.DateTimeField()
    valido_ate = models.DateTimeField()
    
    def __str__(self):
        return f"{self.nome_funcionario} -> {self.curso_funcionario}"
