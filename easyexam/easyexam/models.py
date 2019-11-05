from django.db import models

class Paciente(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    idade = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )

    endereco = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=3,
        null=False,
        blank=False
    )

    altura = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    objetos_pacientes = models.Manager()

class Medico(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    cfm = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    telefone = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )

    especializacao = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    objetos_medicos = models.Manager()

class Exame(models.Model):

    data = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )

    hora = models.CharField(
        max_length=5,
        null=False,
        blank=False
    )

    tipo = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    paciente = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    medico = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    status = models.CharField(
        max_length=254,
        null=False,
        blank=False
    )

    objetos_exames = models.Manager()