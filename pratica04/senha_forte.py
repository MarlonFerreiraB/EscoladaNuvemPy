while True:
    senha = input("Digite uma senha forte com pelo menos 8 carecteres e pelo menos 1 numero: ")
    if len(senha) < 8:
        print("Senha muito curta deve ter pelo menos 8 caracteres")
        continue
    if not any(char.isdigit() for char in senha):
        print("Senha deve conter pelo menos um número")
        continue
    print("Senha forte criada com sucesso!")
    break
