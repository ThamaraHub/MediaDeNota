NotaA=float(input("Informe a primeira nota: "))
NotaB=float(input("Informe a segunda nota: "))

#Calcular media
mediafinal = (NotaA + NotaB) / 2

#Verificacao
if mediafinal >=7.0:
    print("A média: %1.f - Aprovado" % mediafinal)
else:
    print("A média: %1.f - Reprovado" % mediafinal)


