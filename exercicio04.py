#Para mim esse foi o mais completo. deixei comentários.
#Com o 'while' iniciei o laço do loop, caso o 'user' quiser continuar o progama.
#Vou otimizar este código com o tempo.
while True:

#Aqui é o nome do progaminha.
  print("CALCULADORA SIMPLES:")
 
#Aqui declarei minhas Operações.
  soma = "+"
  subtração = "-"
  multiplicação = "*"
  divisão = "/"
  
#Aqui coloquei um detalhe importante. aprendi e usei o 'Try' o 'Except', se o 'user' tentar colocar uma letra no lugar de um número, o terminal exibe o erro.
  try:
    NumberOne = int(input("Por favor, digite um número: "))
    NumberTwo = int(input("Por favor, digite outro número: "))    
    Operação = (input("> Qual operação deseja fazer? +, -, *, / : "))

#Aqui comecei a fazer as operações selecionadas e mandei mostrar no terminal. usando 'If' e o 'Elif'.
    if Operação == "+":
     print(NumberOne + NumberTwo)
  
    elif Operação == "-":
     print(NumberOne - NumberTwo)

    elif Operação == "*":
     print(NumberOne * NumberTwo)
#Aqui coloquei um detalhe importante. aprendi e usei o 'Try' o 'Except', se o 'user' tentar colocar uma letra no lugar de um número, o terminal exibe o erro.

#Aqui coloquei um detalhe importante.  quando o  'user' tentar dividir algo pelo número 0, o terminal deve exibir um erro.
#Também fiz a formatação para dizimas terminar com 3 números depois do ponto.
    elif Operação == "/":
     try:
      operaçãoDiv = NumberOne / NumberTwo
      operaçãoDiv2 = NumberTwo / NumberOne
      print(f'{NumberOne / NumberTwo:.3f}')
     except ZeroDivisionError:
       print("(Oops! Não é possivel dividir por 0. Tente novamente.)") 

#Mensagem de erro de caracter.       
  except ValueError:
   print("(Oops! Isso não é um número válido. Tente Novamente.)")
 
#Estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
   exit()

  