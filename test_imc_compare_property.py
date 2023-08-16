from imc_compare_property import IMC

x = IMC()
y = IMC()
x.height = 2
x.weight = 65
y.height = 2
y.weight = 70

if x == y:
    print("São iguais")
else:
    print("Não são iguais")