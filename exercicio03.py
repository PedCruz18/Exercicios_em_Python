while True:

  print("CONVERTER PARA FAHRENHEIT:")

  try:
    NumberCelcius = int(input("Por favor, digite um número em Celcius: "))
    NumberFahrenheit = NumberCelcius * 9/5 + 32
    print(f'{NumberFahrenheit:.2F}'" Fahrenheit")
  
  except ValueError:
    print("(Oops! Isso não é um número inteiro válido. Tente Novamente.)")

# Estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
    exit()







