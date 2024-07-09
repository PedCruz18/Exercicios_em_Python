# Aqui usei novamente o 'while' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("CONVERTER PARA FAHRENHEIT:")
 
# aqui declarei minha constante e também aprendi o 'Try' o 'Except' e o 'Break'. assim coloquei que o 'user' só pode usar números inteiros.

  try:
    NumberCelcius = int(input("Por favor, digite um número em Celcius: "))
  except ValueError:
    print("(Oops! Isso não é um número inteiro válido. Feche e execute o progama novamente.)")
    input("(Teclhe Enter para fechar)")
    exit()

  NumberFahrenheit = NumberCelcius * 9/5 + 32

# Aqui estou mandando imprimir o resultado da expressão em fahrenheit.  
  print(f'{NumberFahrenheit:.2F}'" Fahrenheit")

# aqui estou retomando o laço do while e perguntando se o 'user' deseja continuar ou não o progaminha.
  saida = input("(Deseja Encerrar? 'S ou N'): ")
 
  if saida == "S":
    break
  if saida == "s":
     break



