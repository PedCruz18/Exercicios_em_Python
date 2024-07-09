
while True: 
  try:
   print("CALCULE SUA MÉDIA:")

   nota01 = float(input("Por favor, digite sua nota 1: "))
   nota02 = float(input("Por favor, digite sua nota 2: "))
   nota03 = float(input("Por favor, digite sua nota 3: "))

   resultado = (nota01 + nota02 + nota03) 
   print("sua média é: "f'{resultado:.2f}') 
      
   saida = input("Deseja Encerrar? 'S ou N'): ")
   
   if saida == "S":
    exit()
   
   if saida == "s":
    exit()
  
  except ValueError:
   print("(Oops! Use apenas números inteiros ou decimais.)")
   saida = input("Deseja Encerrar? 'S ou N'): ")
  
   if saida == "S":
    exit()
  
   if saida == "s":
    exit()


