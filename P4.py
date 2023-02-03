import numpy as np
p1 = float(input("entre com a sua p1:\n"))
p2 = float(input("entre com a sua p2:\n"))
p3 = float(input("entre com a sua p3:\n"))
p4 = float(input("entre com a sua p4:\n"))
n1 = (p1 + p2) / 2
print("A sua média da N1 é:", n1)
n2 = (p3 + p4) / 2
print("A sua média da N2 é:", n2)
mf = (2 * n1 + 3 * n2) / 5
print("A sua média final é:", mf)
if mf >= 6:
    print("Você passou direto!")
elif mf >= 3 and mf < 6:
    for count in np.arange(0, 10, 0.1):
        AF = count + 0.1
        maf = (mf + AF) / 2
        if maf >= 5:
            print(f"Se você tirar a nota mínima para ir para a AF precisará de, no mínimo, {AF: .2f} para passar")
            break
else:
    print("Você reprovou")