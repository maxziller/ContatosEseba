import os
import re

class Contato:
    def __init__(self, numero,nome):
        self.numero = numero
        self.nome = nome


def pegaano(ano):
    turma = ano.replace('ESEBA - ','')
    turma = turma.replace(' - Turma ','')
    turma = turma.replace('° ','')
    turma = turma.replace('Periodo','Per')
    turma = turma.replace('Período','Per')
    return turma


def filtranumero(numero):
    telefone = re.sub('[^0-9]', '', numero)
    return telefone


def juntatuplas(tupla,dicionario):
    if (tupla[0] not in dicionario[0]):
        turma = tupla[0] + "/" + dicionario[0]
    else:
        turma = dicionario[0]
    aluno1 = tupla[1].split(" ",1)
    if (aluno1[0] not in dicionario[1]):
        aluno = aluno1[0] + " e " + dicionario[1]
    else:
        aluno = dicionario[1]
    email = tupla[2]
    return (turma,aluno,email)
    

def quebralinha(line):
    linha = line.strip()
    linha = linha.split(";")
    turma = pegaano(linha[0])
    aluno = linha[1].strip()
    email = ''
    telefones = []
    for elem in linha[2:]:
        if ("@" in elem):
            email = elem
        else:
            palavra = filtranumero(elem)
            if (len(palavra) > 7):
                telefones.append(palavra)
    return (turma,aluno,email,telefones)
    

#Path deve ser modificado para ter o caminho do arquivo com os contatos gerados pela tabela da secretaria escolar
path = 'C:/Users/Administrador/Documents/ListadeContato.csv'
arquivo = open(path, 'r')
telefones = dict()
for line in arquivo:
    tupla = quebralinha(line)
    for tel in tupla[3]:
        if tel in telefones:
            if (tupla[1] != telefones[tel][1]):
                junto = juntatuplas(tupla,telefones[tel])
                telefones[tel] = junto
        else:
            telefones[tel] = (tupla[0],tupla[1],tupla[2])

x = open ("Contatos.csv",'x',encoding='utf8')
x.write("Nome;Telefone;Email;\n")
for tel in telefones:
    nome = telefones[tel][0] + " " + telefones[tel][1]
    telefone = tel
    email = telefones[tel][2]
    x.write(nome +";"+telefone +";"+email+"\n")
x.close()
