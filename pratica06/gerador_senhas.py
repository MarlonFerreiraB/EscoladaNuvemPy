import random
while True:
    tamanhoSenha = int(input("Digite o tamanho da senha:(8,12 ou 16 caracteres) "))
    if tamanhoSenha not in [8, 12, 16]:
        print("Tamanho inválido. Por favor, escolha entre 8, 12 ou 16 caracteres.")
        continue
    senha = ""
    caracteres = r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{};':\\|,.<>/?~`"
    for i in range(tamanhoSenha):
        senha += random.choice(caracteres)
    print("Senha gerada:", senha)
    opcao = input("Deseja gerar outra senha? (s/n) ")
    if opcao.lower() != 's':
        break
