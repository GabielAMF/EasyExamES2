from helloworld.models import Paciente
from random import randint

nomes = ['Gabriel', 'Ana', 'Joao', 'Luis', 'Vitoria']
sobrenomes = ['Cerrado', 'Amelia', 'Junior', 'Silva', 'Moreira']

for i in range(0, 9):
    paciente = Paciente(
        nome=nomes[randint(0,4)],
        sobrenome=sobrenomes[randint(0,4)],
        cpf='015.458.895-5'+str(i),
        idade=3+i+2*i,
        endereco='Rua '+nomes[randint(0,4)]+', numero: '+str(i+4)+', bairro: Icarai, cidade: Niteroi',
        peso = 65,
        altura = 2,
        telefone = '2499876543'+str(i)
    )

    paciente.save()
