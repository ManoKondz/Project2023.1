import numpy as np
p1 = float(input("entre com a sua p1:"))
for count in np.arange(0, 10, 0.1):
    p2 = count + 0.1
    n1 = (p1 + p2) / 2
    if n1 == 6:
        print(f"Sua p2 precisa ser: {p2:.2f}")
        break
    elif p2 == 10:
        print("Você não obterá nota suficiente, tire %s para recuperar nas próximas provas" % (p2))
if n1 == 6:
    print("Você precisa tirar nota 6 na p3"); print("Você precisa tirar nota 6 na p4")
if n1 < 6:
    for count in np.arange(0, 10, 0.1):
        p3 = count + 0.1
        p4 = count + 0.1
        n2 = (p3 + p4) / 2
        mf = (2* n1 + 3 * n2)/5
        if mf >= 6:
            print("Você precisa de, no mínimo, %s na p3 e %s na p4 para passar" % (p3, p4))
            break