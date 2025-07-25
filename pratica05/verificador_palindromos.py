

def ehpalindromo(frase):

    fraseTest = frase.replace(" ", "").lower()
    if fraseTest == fraseTest[::-1]:
        return True
    else:
        return False

frase = input("Digite algo: ")

verificador = ehpalindromo(frase)

if verificador:
    print(f"A frase '{frase}' é um palíndromo")
else:
    print(f"A frase '{frase}' não é um palíndromo")