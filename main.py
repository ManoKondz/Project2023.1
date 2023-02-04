import numpy as np
import smtplib
import email.message
import time

# Funções importantes para o projeto

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
    corpo("<Escolha uma das opções de acordo com a quantidade de avaliaçãos que você já realizou>")
    print("<Digite o número correspondente à opção desejada>")
    c = 1
    for item in lista:
        print(f"{[ c ]} -> {item}")
        c += 1
    print(linha())

# Interface para o menu principal

cabeçalho("Inicializando...")
time.sleep(5)
corpo("Qual nota você precisa para passar?")
time.sleep(2)
while True:
    print(linha())
    corpo("<O programa irá informar as notas das avaliação que você não realizou>")
    menu(["Primeira avaliação ", "Segunda avaliação", "Terceira avaliação", "Quarta avaliação", "Reportar Bug/Sugestões para melhorias", "Sair do Programa"])

# Entrada

    while True:
        opcao = input("Qual item você deseja?\n")
        try:
            opcao = int(opcao)
        except ValueError:
            print("Não é um número válido, Digite somente números válidos.")
        if type(opcao) == int:
            break


# verificador de opção

# Números inexistentes

    if opcao > 6 or opcao < 1:
        print("Opção Inválida, selecione novamente")
        print(linha())
        time.sleep(0.5)
        print("Retornando ao menu...")
        print(linha())
        time.sleep(3)

# Desligar o programa

    if opcao == 6:
        print(
            """<Desligando aplicação>
        Aguarde..."""
        )
        time.sleep(3)
        print("Programa Desligado, Obrigado por utilizar!")
        break
    print(linha())

# avaliação 1

    if opcao == 1:
        while True:
            p1 = input("Digite aqui sua nota da avaliação 1\n")
            try:
                p1 = float(p1)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p1) == float:
                break
        if p1 > 10:
            p1 = 10
        print("Calculando...")
        time.sleep(1)
        for count in np.arange(0, 10, 0.1):
            p2 = count + 0.1
            n1 = (p1 + p2) / 2
            if n1 == 6:
                print(f"Sua p2 precisa ser: {p2:.2f}\n")
                break
            elif p2 == 10:
                print("Você não obterá nota suficiente, tire %s para recuperar nas próximas avaliaçãos\n" % (p2))
        if n1 == 6:
            print("Você precisa tirar nota 6 na p3");
            print("Você precisa tirar nota 6 na p4")
        if n1 < 6:
            for count in np.arange(0, 10, 0.1):
                p3 = count + 0.1
                p4 = count + 0.1
                n2 = (p3 + p4) / 2
                mf = (2 * n1 + 3 * n2) / 5
                if mf >= 6:
                    print("Você precisa de, no mínimo, %s na p3 e %s na p4 para passar" % (p3, p4))
                    break
        print(linha())
        print("Operação Concluída")
        input("Confirme para voltar ao menu")
        print("Retornando ao menu...")
        time.sleep(2)

# avaliação 2

    if opcao == 2:
        while True:
            p1 = input("Digite aqui sua nota da avaliação 1\n")
            try:
                p1 = float(p1)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p1) == float:
                break
        while True:
            p2 = input("Digite aqui sua nota da avaliação 2\n")
            try:
                p2 = float(p2)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p2) == float:
                break
        if p1 > 10:
            p1 = 10
        if p2 > 10:
            p2 = 10
        print("Calculando...")
        time.sleep(1)
        n1 = (p1 + p2) / 2
        print(f"Sua média da N1 é: ", n1)
        for count in np.arange(0, 10, 0.1):
            p3 = count + 0.11
            p4 = count + 0.1
            n2 = (p3 + p4) / 2
            mf = (2 * n1 + 3 * n2) / 5
            if mf >= 6:
                print(f"Você precisa de, no mínimo, {p3: .2f} na p3 e {p4: .2f} na p4 para passar sem ir para a AF")
                break
        for count in np.arange(0, 10, 0.1):
            p3 = count + 0.1
            p4 = count + 0.1
            n2 = (p3 + p4) / 2
            mf = (2 * n1 + 3 * n2) / 5
            if mf >= 3:
                print(f"Você precisa de, no mínimo, {p3: .2f} na p3 e {p4: .2f} na p4 para ir para a AF")
                break
        for count in np.arange(0, 10, 0.1):
            AF = count + 0.1
            maf = (mf + AF) / 2
            if maf >= 5:
                print(
                    f"Se você tirar a nota mínima para ir para a AF precisará de, no mínimo, {AF: .2f} para passar")
                break
        print(linha())
        print("Operação Concluída")
        input("Confirme para voltar ao menu")
        print("Retornando ao menu...")
        time.sleep(2)

# Avaliação 3

    if opcao == 3:
        while True:
            p1 = input("Digite aqui sua nota da avaliação 1\n")
            try:
                p1 = float(p1)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p1) == float:
                break
        while True:
            p2 = input("Digite aqui sua nota da avaliação 2\n")
            try:
                p2 = float(p2)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p2) == float:
                break
        while True:
            p3 = input("Digite aqui sua nota da avaliação 3\n")
            try:
                p3 = float(p3)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p3) == float:
                break
        if p1 > 10:
            p1 = 10
        if p2 > 10:
            p2 = 10
        if p3 > 10:
            p3 = 10
        n1 = (p1 + p2) / 2
        print("Calculando...")
        time.sleep(0.5)
        print("Sua média da N1 é: ", n1)
        print("Calculando...")
        time.sleep(1)
        for count in np.arange(0, 10, 0.1):
            p4 = count + 0.1
            n2 = (p3 + p4) / 2
            mf = (2 * n1 + 3 * n2) / 5
            if mf >= 6:
                print(f"Você precisa de, no mínimo, {p4: .2f} na p4 para passar sem ir para a AF")
                break
        for count in np.arange(0, 10, 0.1):
            p4 = count + 0.1
            n2 = (p3 + p4) / 2
            mf = (2 * n1 + 3 * n2) / 5
            if mf >= 3 and mf < 6:
                print(f"Você precisa de, no mínimo, {p4: .2f} na p4 para ir para a AF")
                break
        if mf >= 3 and mf < 6:
            for count in np.arange(0, 10, 0.1):
                AF = count + 0.1
                maf = (mf + AF) / 2
                if maf >= 5 and maf <= 6:
                    print(f"Se você tirar a nota mínima para ir para a AF precisará de, no mínimo, {AF: .2f} para passar")
                    break
        print(linha())
        print("Operação Concluída")
        input("Confirme para voltar ao menu")
        print("Retornando ao menu...")
        time.sleep(2)

# Avaliação 4

    if opcao == 4:
        while True:
            p1 = input("Digite aqui sua nota da avaliação 1\n")
            try:
                p1 = float(p1)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p1) == float:
                break
        while True:
            p2 = input("Digite aqui sua nota da avaliação 2\n")
            try:
                p2 = float(p2)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p2) == float:
                break
        while True:
            p3 = input("Digite aqui sua nota da avaliação 3\n")
            try:
                p3 = float(p3)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p3) == float:
                break
        while True:
            p4 = input("Digite aqui sua nota da avaliação 4\n")
            try:
                p4 = float(p4)
            except ValueError:
                print("Não é um número válido, Digite somente números válidos.")
            if type(p4) == float:
                break
        if p1 > 10:
            p1 = 10
        if p2 > 10:
            p2 = 10
        if p3 > 10:
            p3 = 10
        if p4 > 10:
            p4 = 10
        n1 = (p1 + p2) / 2
        print("Calculando...")
        time.sleep(0.5)
        print("A sua média da N1 é:", n1)
        n2 = (p3 + p4) / 2
        print("Calculando...")
        time.sleep(0.5)
        print("A sua média da N2 é:", n2)
        mf = (2 * n1 + 3 * n2) / 5
        print("Calculando...")
        time.sleep(0.5)
        print("A sua média final é:", mf)
        print("Calculando...")
        time.sleep(1)
        if mf >= 6:
            print("Você passou direto!")
        elif mf >= 3 and mf < 6:
            for count in np.arange(0, 10, 0.1):
                AF = count + 0.1
                maf = (mf + AF) / 2
                if maf >= 5:
                    print(
                        f"Se você tirar a nota mínima para ir para a AF precisará de, no mínimo, {AF: .2f} para passar")
                    break
        else:
            print("Você reprovou")
        print(linha())
        print("Operação Concluída")
        input("Confirme para voltar ao menu")
        print("Retornando ao menu...")
        time.sleep(2)

# Reportar Bugs e Sugestões

    if opcao == 5:
        print("Loading...")
        time.sleep(5)
        print("Reporte o bug")
        print("Após enviar, espere alguns segundos para confirmação")

        assunto_email = input("Digite o assunto do email:\n")


        def enviar_email():
            corpo_email = input("""
        Para criar um parágrafo utilize:
        <p>Parágrafo1</p>
        <p>Parágrafo2</p>
            """)

            msg = email.message.Message()
            msg['Subject'] = assunto_email
            msg['From'] = 'Nota.necessaria2023@gmail.com'
            msg['To'] = 'Nota.necessaria2023@gmail.com'
            password = 'cbxhznbyqqeiovcw'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print('Email enviado')



        enviar_email()
    print(linha())
    print("Operação Concluída")
    input("Confirme para voltar ao menu")
    print("Retornando ao menu...")
    time.sleep(2)