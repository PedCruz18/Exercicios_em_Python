#Aqui aprendi sobre o ''while'' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("VERIFICAÇÃO DE PAR OU ÍMPAR:")
 
# aqui declarei minhas 'var'.
  Number = int(input("Digite um número >> "))

# aqui estou fazendo o número escolhido ser dividido por 2, e após isso
# verificar se é diferente de 0 ou não. 
  Number2 = Number % 2

  if Number2 == 0:
    print(">> "f'{Number}'" é Par")
 
  else:
    print(">> "f'{Number}'" é Ímpar")

# aqui estou retomando o laço do while e perguntando se o 'user' deseja continuar ou não o progaminha.
  saida = input("Deseja Encerrar? 'S ou N' ")
 
  if saida == "S":
    break
  if saida == "s":
     break
