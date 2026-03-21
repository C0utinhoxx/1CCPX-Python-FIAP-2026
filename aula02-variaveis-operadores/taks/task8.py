valorProduto = float(input("Digite o valor do produto: R$ "))
valorPago = float(input("Digite o valor pago pelo cliente: R$ "))

troco = valorPago - valorProduto

print(f"O valor do troco é: R$ {troco:.2f}")