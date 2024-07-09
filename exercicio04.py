# Aqui aprendi sobre o ''while'' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("CALCULADORA SIMPLES:")
 
# aqui declarei minhas 'var'.
  soma = "+"
  subtração = "-"
  multiplicação = "*"
  divisão = "/"
  
  try:
    NumberOne = int(input("Por favor, digite um número: "))
    NumberTwo = int(input("Por favor, digite outro número: "))
  except ValueError:
    print("Oops! Isso não é um número válido. Feche e execute o progama novamente.")
    input("(Teclhe Enter para fechar)")
  
    Operação = (input("> Qual operação deseja fazer? +, -, *, / : "))

# aqui comecei a fazer as operações selecionadas e mandei mostrar no terminal.
  if Operação == "+":
    print(NumberOne + NumberTwo)
  
  elif Operação == "-":
    print(NumberOne - NumberTwo)

  elif Operação == "*":
    print(NumberOne * NumberTwo)

# aqui coloquei um detalhe importante. aprendi e usei o 'Try' e 'Except' para quando o  'user' tentar dividir
# algo pelo número 0, o terminal exibir um erro. também fiz a formatação para dizimas terminar com 3 números depois do ponto.
  elif Operação == "/":
   try:
     operaçãoDiv = NumberOne / NumberTwo
     operaçãoDiv2 = NumberTwo / NumberOne
     print(f'{NumberOne / NumberTwo:.3f}')
   except ZeroDivisionError:
    print("(Oops! não é possivel dividir por 0. Tente novamente..)") 

# aqui estou retomando o laço do while e perguntando se o 'user' deseja continuar ou não o progaminha.
  saida = input("(Deseja Encerrar? 'S ou N'): ")
 
  if saida == "S":
    break
  if saida == "s":
     break
  if saida == "Sim":
    break
  if saida == "sim":
     break
  