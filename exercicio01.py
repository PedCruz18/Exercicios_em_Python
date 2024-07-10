
while True: 
  try:
   print("VERIFICAÇÃO DE IDADE PARA VOTAR:")
   IdadeUser = int(input("Por favor, digite a sua Idade: "))
   
   if IdadeUser >= 16:
    print("> você PODE votar :)") 
   
   else:
    print("> você NÃO pode votar :(")

  except ValueError:
   print("(Oops! Essa não é uma Idade válida. Tente Novamente.)")

# Estruta de fechar o progama.
   saida = input("Deseja Encerrar? 'S ou N'): ")
   if saida == "S" or saida == "s":
    exit()


