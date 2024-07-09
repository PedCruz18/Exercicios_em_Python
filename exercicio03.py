# Aqui usei novamente o 'while' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("CONVERTER PARA FAHRENHEIT:")
 
# aqui declarei minha constante e também aprendi o 'Try' o 'Except' e o 'Break'. assim coloquei que o 'user' só pode usar números inteiros.

  try:
    NumberCelcius = int(input("Por favor, digite um número em Celcius: "))
    NumberFahrenheit = NumberCelcius * 9/5 + 32
    print(f'{NumberFahrenheit:.2F}'" Fahrenheit")
 
    saida = input("(Deseja Encerrar? 'S ou N'): ")    
  except ValueError:
    print("(Oops! Isso não é um número inteiro válido. Feche e execute o progama novamente.)")
    input("(Teclhe Enter para fechar)")
 
  if saida == "S":
    break
  if saida == "s":
     break



