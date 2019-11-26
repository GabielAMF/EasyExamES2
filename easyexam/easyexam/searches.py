from easyexam.models import Paciente, Medico, Exame

#menus de opcoes de busca
#1: buscas para paciente
#2: buscas para medico
#3: buscas para exames
def menu_buscas(id, nome, sobrenome, cpf, cfm, especializacao, tipo, paciente, medico, status):
    resp = ""
    if id == 1:
        resp = busca_paciente(nome, sobrenome, cpf)
    else if id == 2:
        resp = busca_medico(nome, sobrenome, cpf, cfm, especializacao)
    else if id == 3:
        resp = busca_exame(tipo, paciente, medico, status)
    else:
        resp = "indice de busca invalido"
    return resp

#opcoes de busca de paciente
#1.1: buscar todos os pacientes
#1.2: buscar paciente por nome
#1.3: buscar paciente por sobrenome
#1.4: buscar por cpf
#----opcoes avancadas (nao inseridas)---
#1.5: buscar por idade menor que
#1.6: buscar por idade maior que
#1.7: buscar por peso menor que
#1.8: buscar por peso maior que
#1.9: buscar por altura menor que
#1.10: buscar por altura maior que
#----------------------------------------
def busca_paciente(nome, sobrenome, cpf):#, idade_max, idade_min, peso, altura):
    if nome != None:
        pacientes = Paciente.objetos_pacientes
            .filter(nome__startswith=nome)
            .all()
    else if sobrenome != None:
        pacientes = Paciente.objetos_pacientes
            .filter(sobrenome__startswith=sobrenome)
            .all()  
    else if cpf != None:
        pacientes = Paciente.objetos_pacientes
            .filter(cpf__startswith=cpf)
            .all()
    else:
        pacientes = Paciente.objetos_pacientes.all()
    return pacientes
    '''
    else if idade != None:
        pacientes = Paciente.objetos_pacientes
            .filter(idade__lt=idade)
            .all()
    else if index == 16:
        pacientes = Paciente.objetos_pacientes
            .filter(idade__gt=idade)
            .all()
    else if index == 17:
        pacientes = Paciente.objetos_pacientes
            .filter(peso__lt=peso)
            .all()
    else if index == 18:
        pacientes = Paciente.objetos_pacientes
            .filter(peso__gt=peso)
            .all()
    else if index == 19:
        pacientes = Paciente.objetos_pacientes
            .filter(altura__lt=altura)
            .all()
    else if index == 110:
        pacientes = Paciente.objetos_pacientes
            .filter(altura__gt=altura)
            .all()
    '''

#opcoes de busca de medico
#2.1: buscar todos os medicos
#2.2: buscar medico por nome
#2.3: buscar medico por sobrenome
#2.4: buscar por cpf
#2.5: buscar por cfm
#2.6: buscar por especializacao
def busca_medico(nome, sobrenome, cpf, cfm, especializacao):
    if nome != None:
        medicos = Medico.objetos_medicos
            .filter(nome__startswith=nome)
            .all()
    else if sobrenome != None:
        medicos = Medico.objetos_medicos
            .filter(sobrenome__startswith=sobrenome)
            .all()
    else if cpf != None:
        medicos = Medico.objetos_medicos
            .filter(cpf__startswith=cpf)
            .all()
    else if cfm != None:
        medicos = Medico.objetos_medicos
            .filter(cfm__startswith=cfm)
            .all()
    else if especializacao != None:
        medicos = Medico.objetos_medicos
            .filter(especializacao__startswith=especializacao)
            .all()
    else:
        medicos = Medico.objetos_medicos.all()
    return medicos

#opcoes de busca de exame
#3.1: buscar todos os exames
#3.2: buscar exame por tipo
#3.3: buscar exame por paciente
#3.4: buscar exame por medico
#3.5: buscar exame por status
def busca_exame(tipo, paciente, medico, status):
    if tipo != None:
        exames = Exame.objetos_exames
            .filter(tipo__startswith=tipo)
            .all()
    else if paciente != None:
        exames = Exame.objetos_exames
            .filter(paciente__startswith=paciente)
            .all()
    else if medico != None:
        exames = Exame.objetos_exames
            .filter(medico__startswith=medico)
            .all()
    else if status != None:
        exames = Exame.objetos_exames
            .filter(status__startswith=status)
            .all()
    else:
        exames = Exame.objetos_exames.all()
    return exames