def calcularGorjeta(valorConta,porcentoGorjeta):
    totalGorjeta = valorConta * (porcentoGorjeta/100)
    return totalGorjeta


conta = float(input("Insira o valor da conta: "))
porcento = int(input("Insira o valor da porcentagem: "))
valorGorjeta = calcularGorjeta(conta,porcento)
print(f"o valor da gorjeta é de: {valorGorjeta:.2f}")