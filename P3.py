import numpy as np
p1 = float(input("entre com a sua p1:\n"))
p2 = float(input("entre com a sua p2:\n"))
n1 = (p1 + p2) / 2
print(f"Sua média da N1 é: ", n1)
p3 = float(input("entre com a sua p3:\n"))
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
    if mf >= 3:
        print(f"Você precisa de, no mínimo, {p4: .2f} na p4 para ir para a AF")
        break
for count in np.arange(0,10,0.1):
    AF = count + 0.1
    maf = (mf + AF) / 2
    if maf >= 5:
        print(f"Se você tirar a nota mínima para ir para a AF precisará de, no mínimo, {AF: .2f} para passar")
        break