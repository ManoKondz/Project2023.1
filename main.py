import numpy as np
import smtplib
import email.message
import time
def linha(tam=42):
    return "-=" * tam
def cabeçalho(txt):
    print(linha())
    print(txt.center(84))
    print(linha())
def corpo(txt):
    print(txt.center(84))
    print(linha())
def menu(lista):
    corpo("<Menu Principal>")
    corpo("<Escolha uma das opções de acordo com a quantidade de provas que você já realizou>")
    print("<Digite o número correspondente à opção desejada>")
    c = 1
    for item in lista:
        print(f"{[ c ]} -> {item}")
        c += 1
    print(linha())
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=Separação-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--==-
cabeçalho("Inicializando...")
# time.sleep(5)
cabeçalho("Qual nota você precisa para passar?")
corpo("<O programa irá informar as notas das provas que você não realizou>")
menu(["Primeira Prova", "Segunda Prova", "Terceira Prova", "Quarta Prova", "Reportar Bug", "Sair do Programa"])
