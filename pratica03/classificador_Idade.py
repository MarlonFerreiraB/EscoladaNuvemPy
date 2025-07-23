age = int(input("Digite a idade: "))

if age > 0 and age <= 12: 
    print("Criança")
elif age > 12 and age <= 17:
    print("Adolescente")
elif age > 17 and age <= 59:
    print("Adulto")
elif age >= 60:
    print("Idoso")