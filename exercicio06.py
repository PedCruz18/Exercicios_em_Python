
while True: 
  print("CALCULE SUA MÉDIA:")

  try:

   nota01 = float(input("Por favor, digite sua nota 1: "))
   nota02 = float(input("Por favor, digite sua nota 2: "))
   nota03 = float(input("Por favor, digite sua nota 3: "))

   resultado = (nota01 + nota02 + nota03) / 3
   print("sua média é: "f'{resultado:.2f}') 
      
  except ValueError:
   print("(Oops! Use apenas números inteiros ou decimais.)")

# estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
   exit()
