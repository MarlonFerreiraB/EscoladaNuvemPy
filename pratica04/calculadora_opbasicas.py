while True:
    try:
        sinal = input("Digite o sinal da operação (+, -, *, /): ").strip()
        if sinal not in ['+', '-', '*', '/']:
            print("Sinal inválido. Tente novamente.")
            continue
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if sinal == '+':
            resultado = num1 + num2
        elif sinal == '-':
            resultado = num1 - num2
        elif sinal == '*':
            resultado = num1 * num2
        elif sinal == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = num1 / num2
        print(f"O resultado da operação {num1} {sinal} {num2} é: {resultado}")
        break
    except (ValueError, ZeroDivisionError):
        print("Entrada inválida. Por favor, digite números válidos.")
        continue