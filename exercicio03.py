while True:

  print("CONVERTER PARA FAHRENHEIT:")

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



