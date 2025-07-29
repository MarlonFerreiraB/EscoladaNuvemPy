import csv

pessoas = [
    ["Ana", 28, "São Paulo"],
    ["Jorge", 35, "Rio de Janeiro"],
    ["Lucas", 22, "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ")

try:
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerows(pessoas)
    print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")
except Exception as e:
    print(f"Erro ao gravar o arquivo: {e}")