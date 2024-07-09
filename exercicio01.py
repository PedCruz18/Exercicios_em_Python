

 # aqui é o nome do progaminha.
print("VERIFICAÇÃO DE IDADE PARA VOTAR:")
 
# aqui declarei minha constante
while True: 
  try:
   
   IdadeUser = int(input("Por favor, digite a sua Idade: "))
   
   if IdadeUser >= 16:
    print(">> você PODE votar :)") 
   
   else:
    print(">> você NÃO pode votar :(")
   saida = input("Deseja Encerrar? 'S ou N'): ")
   
   if saida == "S":
    exit()
   
   if saida == "s":
    exit()
  
  except ValueError:
   print("(Oops! Essa não é uma Idade válida. Feche e execute o progama novamente.)")
   saida = input("Deseja Encerrar? 'S ou N'): ")
  
   if saida == "S":
    exit()
  
   if saida == "s":
    exit()


