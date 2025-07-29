import json

dados_pessoa = [
    ["Ana", 28, "São Paulo"],
    ["Jorge", 35, "Rio de Janeiro"],
    ["Lucas", 22, "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo json: ")

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados_pessoa, f, ensure_ascii=False, indent=4)
    print("Dados salvos com sucesso!")
except Exception as e:
    print(f"Erro ao salvar os dados: {e}")

try:
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        dados_carregados = json.load(f)
    print("Dados carregados do arquivo:")
    print(dados_carregados)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Erro ao ler os dados: {e}")