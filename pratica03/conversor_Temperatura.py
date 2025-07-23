temperatura = float(input("Digite a temperatura: "))
unidade = input("Digite a unidade (C para Celsius, F para Fahrenheit ou K para Kelvin): ").upper()
converter = input("Converter para (C para Celsius, F para Fahrenheit ou K para Kelvin): ").upper()
if unidade == 'C':
    if converter == 'F':
        temperatura_convertida = (temperatura * 9/5) + 32
        print(f"{temperatura}°C é igual a {temperatura_convertida}F")
    elif converter == 'K':
        temperatura_convertida = temperatura + 273.15
        print(f"{temperatura}°C é igual a {temperatura_convertida}K")
    else:
        print("Unidade de conversão inválida.")
elif unidade == 'F':
    if converter == 'C':
        temperatura_convertida = (temperatura - 32) * 5/9
        print(f"{temperatura}°F é igual a {temperatura_convertida}C")
    elif converter == 'K':
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
        print(f"{temperatura}°F é igual a {temperatura_convertida}K")
    else:
        print("Unidade de conversão inválida.")
elif unidade == 'K':
    if converter == 'C':
        temperatura_convertida = temperatura - 273.15
        print(f"{temperatura}K é igual a {temperatura_convertida}C")
    elif converter == 'F':
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
        print(f"{temperatura}K é igual a {temperatura_convertida}F")
    else:
        print("Unidade de conversão inválida.")