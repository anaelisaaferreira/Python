nome_produto = input ("Digite o nome do produto: ")
preco = float(input("Digite o preco do produto: "))
desconto = float (input( "Digite o percentual de desconto : "))
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto
print (f"Produto : {nome_produto} - preco final : R$ {preco_final}")
