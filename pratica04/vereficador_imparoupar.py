par = []
impar = []
while True:
    numero = input("Digite um número inteiro (ou 'sair' para encerrar): ")
    if numero.lower() == 'fim':
        print("tiveram",len(par), "números pares e", len(impar), "números ímpares.")
        print("Programa encerrado.")
        break
    try:
        numero_int = int(numero)
        if numero_int % 2 == 0:
            print(f"{numero_int} é um número par.")
            par.append(numero_int)
        else:
            print(f"{numero_int} é um número ímpar.")
            impar.append(numero_int)
    except ValueError:
        print("Entrada inválida por favor, digite um número inteiro ou 'fim'.")