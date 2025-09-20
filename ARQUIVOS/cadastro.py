# Solicitando os dados para o cadrasto
nome_completo = input ("Digite seu nome: ")
email = input ("Digite seu gmail: ")

# Criando o arquivo pessoa.txt para gravação dos dados
arquivo = open ("pessoa.txt", "a")
arquivo.write(f"{nome_completo} | {email}")
arquivo.close()

