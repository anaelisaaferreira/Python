programa {
  funcao inicio() {
    cadeia nome
    inteiro nota_1
    inteiro nota_2
    inteiro nota_3
    real media 

   escreva ("Digite o nome do aluno: ")
   leia (nome)
   escreva ("Digite a 1ª nota: ") 
   leia (nota_1)
   escreva ("Digite a 2ª nota: ")
   leia (nota_2)
   escreva ("Digite a 3ª nota: ")
   leia (nota_3)

   media = (nota_1 + nota_2 + nota_3) / 3

   escreva ("Bom dia " , nome," sua média é ", media)
