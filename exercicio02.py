while True:

  print("VERIFICAÇÃO DE PAR OU ÍMPAR:")

  try:

    Number = int(input("> Por favor, digite um número: "))
    Number2 = Number % 2

    if Number2 == 0:
     print("> "f'{Number}'" é Par")
 
    else:
     print("> "f'{Number}'" é Ímpar") 

  except ValueError:
    print("(Oops! Isso não é um número inteiro válido, Tente Novamente.)")
 
# Estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
    exit()
