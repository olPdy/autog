import requests

api_key = 'coinrankinged42fa8cfac494d903871119037f1ce6958c5c09927dfeae'
base_url = 'https://api.coinranking.com/v2'
headers = {'x-access-token': api_key}

try:
    # 1. Получить криптовалюты с 150 по 200 места в топе
    coins_url = f'{base_url}/coins'
    params = {'offset': 150, 'limit': 50}
    coins_response = requests.get(coins_url, headers=headers, params=params)
    coins_data = coins_response.json()

    if 'data' not in coins_data:
        print("Ошибка при получении данных о криптовалютах:", coins_data)
    else:
        # Вывод списка криптовалют с 150 по 200 места
        print("Криптовалюты с 150 по 200 место в топе:")
        for index, coin in enumerate(coins_data['data']['coins']):
            print(f"{index + 151}. {coin['name']} ({coin['symbol']})")

        # 2. Получить цены криптовалют
        print("\nЦены криптовалют:")
        for coin in coins_data['data']['coins']:
            print(f"{coin['name']} ({coin['symbol']}): ${coin['price']}")

        # 3. Получить исторические данные криптовалют (например, за последние 30 дней)
        print("\nИсторические данные криптовалют за последние 30 дней:")
        for coin in coins_data['data']['coins']:
            history_url = f"{base_url}/coin/{coin['uuid']}/history"
            history_params = {'timeframe': '30d'}
            history_response = requests.get(history_url, headers=headers, params=history_params)
            history_data = history_response.json()
            
            if 'data' not in history_data:
                print(f"Ошибка при получении исторических данных для {coin['name']} ({coin['symbol']}):", history_data)
            else:
                print(f"{coin['name']} ({coin['symbol']}):")
                for history_item in history_data['data']['history']:
                    print(f"  {history_item['timestamp']} - ${history_item['price']}")
except Exception as e:
    print("Произошла ошибка:", e)
