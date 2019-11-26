from easyexam.models import Paciente, Medico, Exame
from random import randint

#insercao de pacientes no banco
nomes_p = ['Gabriel', 'Ana', 'Joao', 'Luis', 'Vitoria']
sobrenomes_p = ['Cerrado', 'Amelia', 'Junior', 'Silva', 'Moreira']

for i in range(0, 9):
    paciente = Paciente(
        nome=nomes_p[randint(0,4)],
        sobrenome=sobrenomes_p[randint(0,4)],
        cpf='015.458.895-5'+str(i),
        idade=3+i+2*i,
        endereco='Rua '+nomes_p[randint(0,4)]+', numero: '+str(i+4)+', bairro: Icarai, cidade: Niteroi',
        peso = 65,
        altura = 2,
        telefone = '2499876543'+str(i)
    )

    paciente.save()

#insercao de medicos no banco
nomes_m = ['Ana', 'Jorge', 'Marco', 'Gustavo', 'Rubens', 'Marilia']
sobrenomes_m = ['Magalhaes', 'Botero', 'Ferreira', 'Augusto', 'Nicolau']
especializacao_m = ['Cardiologista', 'Pediatra', 'Neurologista', 'Medico Geral']
for i in range(0, 9):
    medico = Medico(
        nome=nomes_m[randint(0,5)],
        sobrenome=sobrenomes_m[randint(0,4)],
        cpf='015.458.895-5'+str(i),
        cfm='089.150.458-9'+str(i),
        email='doctor_'+nome+'@gmail.com',
        telefone = '2492573243'+str(i),
        especializacao=especializacao_m[randint(0,3)]
    )

    medico.save()

#insercao de exames no banco
tipo_e = ['Cardiovascular', 'Neurologico', 'Urina', 'Sangue', 'Tomografia']
status_e = ['Encaminhado', 'Em espera', 'Em andamento', 'Concluido', 'Com resultados']
for i in range(0,9):
    exame = Exame(
        data='1'+str(i)+'/0'+str(i)+'/201'+str(i),
        hora='1'+str(i)+':3'+str(i),
        tipo=tipo_e[randint(0,4)],
        paciente=nomes_p[randint(0,4)]+' '+sobrenomes_p[randint(0,4)],
        medico=nomes_m[randint(0,5)]+' '+sobrenomes_m[randint(0,4)],
        status=status_e[randint(0,4)]
    )

    exame.save()