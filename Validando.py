while True:
    Var = input("Entrada:\n")
    try:
        Var = float(Var)
    except ValueError:
        print("Não é um número válido, Digite somente números válidos.")
    if type(Var) == float:
        break