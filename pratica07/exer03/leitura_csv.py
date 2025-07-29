import csv

filename = input("Digite o nome do arquivo CSV: ")

try:
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            print(r)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")