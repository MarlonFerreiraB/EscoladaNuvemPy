print("Conversor de moeda")
print("Digite o valor em reais:")
valor = 100.00
print("Dolar(1)")
print("Euro(2)")
opc = int(input("Escolha a moeda para conversão: "))
if opc == 1:
    totalD = valor * 5.20
    print(f"Valor em dolares: {totalD:.2f}")
elif opc == 2:
    totalE = valor * 6.15
    print(f"Valor em euros: {totalE:.2f} ")