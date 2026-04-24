def validar_nota(nota):
    while nota < 0 or nota > 10:
        print("Voce é burrão hein")
        nota = float(input("Digite a nota novamente: "))
    return nota

notaA = float(input("Digite e 1 nota:"))
notaA = validar_nota(notaA)

notaB = float(input("Digite e 2 nota:"))
notaB = validar_nota(notaB)

media = (notaA + notaB) / 2
print(media)