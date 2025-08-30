import requests

awesome = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

requisicao = requests.get(awesome)
print (requisicao)

dolar_real = float (requisicao.json()['USDBRL']['bid'])
euro_real = float (requisicao.json()['EURBRL']['bid'])
bitcoin_real = float (requisicao.json()['BTCBRL']['bid'])

valor_real = float(input("Digite o valor em R$: "))

print(f"{valor_real:.2f} em dolar $ {valor_real/ dolar_real:.2f}")
print(f"{valor_real:.2f} em euro € {valor_real/ euro_real:.2f}")
print(f"{valor_real:.2f} em bitcoin  {valor_real/ bitcoin_real:.2f}")
