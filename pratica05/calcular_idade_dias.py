anoNaciment =int(input("Digite sua data de nasceimento: "))

def idadeEmDias(nascimento):
    anoAtual = 2025
    idade = anoAtual - nascimento
    return idade * 365

print(idadeEmDias(anoNaciment)," dias" )