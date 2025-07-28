import requests
import datetime



while True:
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()

    if not moeda:
        print("Código da moeda não pode ser vazio. Tente novamente.")
        continue


    try:
        print(f"Buscando cotação para {moeda}/BRL...")
        response = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL", timeout=10)
        response.raise_for_status()

        dados = response.json()


        chave_cotacao = f"{moeda}BRL"

        if chave_cotacao not in dados:
    
            print(f"Código de moeda inválido ou cotação para '{moeda}' não encontrada.")
            print("Por favor, verifique o código da moeda .")
            continue
        
        cotacao = dados[chave_cotacao]


        nome_moeda = cotacao.get('name', 'N/A').replace('/BRL', '')
        valor_atual = float(cotacao.get('bid', '0')) 
        valor_maximo = float(cotacao.get('high', '0'))
        valor_minimo = float(cotacao.get('low', '0'))
        timestamp_str = cotacao.get('timestamp', None)


        data_hora_atualizacao = "N/A"
        if timestamp_str:
            try:
                timestamp = int(timestamp_str)
                data_hora = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)
                data_hora_local = data_hora - datetime.timedelta(hours=3)
                data_hora_atualizacao = data_hora_local.strftime('%d/%m/%Y %H:%M:%S')
            except (ValueError, TypeError):
                data_hora_atualizacao = "Timestamp inválido"

        print(f"\nCotação de {nome_moeda}/BRL")
        print(f"Cotação Atual (Compra): R$ {valor_atual:.4f}")
        print(f"Valor Máximo (dia): R$ {valor_maximo:.4f}")
        print(f"Valor Mínimo (dia): R$ {valor_minimo:.4f}")
        print(f"Última Atualização: {data_hora_atualizacao}")

        break 

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print(f"Erro 404: Cotação para '{moeda}' não encontrada.")
        else:
            print(f"Erro HTTP: {e}")
            print("Não foi possível obter a cotação. O servidor retornou um erro.")
        break 
