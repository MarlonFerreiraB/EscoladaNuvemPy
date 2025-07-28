import requests
try:
    response = requests.get("https://randomuser.me/api/", timeout=10)
    
    dados = response.json()
    usuario =  dados['results'][0]
    nome = usuario['name']
    sobrenome = usuario['name']['last']
    email = usuario['email']
    pais = usuario['location']['country']
    print(f"Nome: {nome['first']} {sobrenome}")
    print(f"E-mail: {email}")
    print(f"País: {pais}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao obter dados do usuário: {e}")
except requests.exceptions.Timeout as e:
    print(f"Tempo limite excedido: {e}")