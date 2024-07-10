
while True: 
  try:
   print("VERIFICAÇÃO DE IDADE PARA VOTAR:")
   IdadeUser = int(input("Por favor, digite a sua Idade: "))
   
   if IdadeUser >= 16:
    print("> você PODE votar :)") 
   
   else:
    print("> você NÃO pode votar :(")
    
   saida = input("Deseja Encerrar? 'S ou N'): ")
   
   if saida == "S":
    exit()
   
   if saida == "s":
    exit()
  
  except ValueError:
   print("(Oops! Essa não é uma Idade válida. Tente Novamente.)")
   saida = input("Deseja Encerrar? 'S ou N'): ")
  
   if saida == "S":
    exit()
  
   if saida == "s":
    exit()


