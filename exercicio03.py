# Aqui usei novamente o 'while' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("CONVERTER PARA FAHRENHEIT:")
 
# aqui declarei minhas 'var'.
  NumberCelcius = int(input("Digite um número em Celcius >> "))
  NumberFahrenheit = NumberCelcius * 9/5 + 32

# Aqui estou mandando imprimir o resultado da expressão em fahrenheit.  
  print(f'{NumberFahrenheit:.2F}')

# aqui estou retomando o laço do while e perguntando se o 'user' deseja continuar ou não o progaminha.
  saida = input("(Deseja Encerrar? 'S ou N'): ")
 
  if saida == "S":
    break
  if saida == "s":
     break



