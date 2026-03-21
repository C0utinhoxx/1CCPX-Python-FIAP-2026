nome1 = input("Nome da peça 1: ")
quant1 = int(input(f"Quantidade de {nome1}: "))
valor1 = float(input(f"Valor unitário de {nome1}: "))

nome2 = input("Nome da peça 2: ")
quant2 = int(input(f"Quantidade de {nome2}: "))
valor2 = float(input(f"Valor unitário de {nome2}: "))

total = (quant1 * valor1) + (quant2 * valor2)

print(f"\nResumo da compra:")
print(f"{quant1}x {nome1} e {quant2}x {nome2}")
print(f"Total a pagar: R$ {total:.2f}")