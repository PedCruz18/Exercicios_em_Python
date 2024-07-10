
while True:   
  try:
     print("VERIFICAÇÃO DE FORMATAÇÃO:")

     NumInt = int(input("Por favor, digite um número inteiro: "))
     NumFlo = float(input("Por favor, digite um número decimal: "))
     UmaStr = str(input("Por Favor, digite uma palavra: "))

     print(f'"O caracter > {NumInt}'" é de Classe <'Int'>")
     print(f'"O caracter > {NumFlo:.2f}'" é de Classe <'Float'>")
     print(f'"O caracter > {UmaStr}'" é de Classe <'Str'>")

  except ValueError:
    print("(Oops! Esse não é um formato válido. Tente Novamente.)")

# estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
      exit()


