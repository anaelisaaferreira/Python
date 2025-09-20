`nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))`

`IMC = peso/(altura**2)`

`print("\nCálculo do IMC")
print(f"Olá {nome}, seu IMC é: {IMC:.2f}")
print (IMC)
if IMC < 18.5:
print("ABAIXO DO PESO, CUIDADO COM A SAUDE!")
elif IMC <= 24.9:
print("PESO NORMAL, TUDO OK!")
elif IMC <= 29.9:
print ("SOBREPESO, CUIDADO COM A SAUDE!")
elif IMC <= 34.9:
print ("OBESIDADE GRAU I, CUIDADO COM A SAUDE!")
elif IMC <= 39.9:
print ("OBESIDADE GRAU II, CUIDADO COM A SAUDE!")
else:
print ("OBESIDADE GRAU III, CUIDADO COM A SAUDE!")`
