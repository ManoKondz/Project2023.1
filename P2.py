import numpy as np
p1 = float(input("entre com a sua p1:\n"))
p2 = float(input("entre com a sua p2:\n"))
n1 = (p1 + p2) / 2
print(f"Sua média da N1 é: ", n1)
if n1 == 6:
    print("Você precisa tirar nota 6 na p3"); print("Você precisa tirar nota 6 na p4")
for count in np.arange(0, 10, 0.1):
        p3 = count + 0.1
        p4 = count + 0.1
        n2 = (p3 + p4) / 2
        mf = (2 * n1 + 3 * n2) / 5
        if mf >= 6:
            print(f"Você precisa de, no mínimo, {p3: .2f} na p3 e {p4: .2f} na p4 para passar")
            break
