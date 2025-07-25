def calcularDesconto(valorConta,porcentoGorjeta):
    totalDesconto = valorConta * (porcentoGorjeta/100)
    return valorConta - totalDesconto


conta = float(input("Insira o valor da conta: "))
porcento = int(input("Insira o valor da porcentagem: "))
valorFinal = calcularDesconto(conta,porcento)
print(f"o valor da gorjeta é de: {valorFinal:.2f}")