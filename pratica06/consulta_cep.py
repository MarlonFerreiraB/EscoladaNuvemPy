import requests
try:
    cep = input("Digite o CEP (somente números): ")
    if not cep.isdigit() or len(cep) != 8:
        raise ValueError("CEP inválido. Deve conter 8 dígitos numéricos.")
    
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=10)
    response.raise_for_status() 
 

    dados = response.json()
    logradouro = dados.get('logradouro', 'Não encontrado')
    bairro = dados.get('bairro', 'Não encontrado')
    cidade = dados.get('localidade', 'Não encontrado')
    estado = dados.get('uf', 'Não encontrado')
    cep_formatado = dados.get('cep', 'Não encontrado')
    print(f"CEP: {cep_formatado}")
    print(f"Logradouro: {logradouro}")
    print(f"Bairro: {bairro}")
    print(f"Cidade: {cidade}")
    print(f"Estado: {estado}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao obter dados do CEP: {e}")

except requests.exceptions.HTTPError as e:
    if response.status_code == 400: 
        print(f"Erro: O CEP '{cep}' parece estar mal formatado na requisição.")
    else:
        print(f"Erro HTTP: {e}")
        print("Não foi possível obter os dados do CEP. O servidor retornou um erro.")