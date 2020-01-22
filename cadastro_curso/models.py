from django.db import models

class cadastroCurso(models.Model):
    #Campos destinados para banco de dados dos cursos cadastrados.
    nome_curso = models.CharField(max_length=64)
    validade_curso = models.IntegerField(default=365)
    norma_curso = models.CharField(max_length=64)
    carga_hora_curso = models.IntegerField()

    def __str__(self):
        return f"{str(self.nome_curso).upper()}"