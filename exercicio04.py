# para mim esse foi o mais completo. então deixei comentários.
# com o 'while' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

# aqui é o nome do progaminha.
  print("CALCULADORA SIMPLES:")
 
# aqui declarei minhas Constantes.
  soma = "+"
  subtração = "-"
  multiplicação = "*"
  divisão = "/"
  

# Aqui coloquei um detalhe importante. aprendi e usei o 'Try' o 'Except' e o 'Break' para se o 'user' tentar colocar uma letra no lugar de um número, o terminal exibe o erro.
# Inicio do loop inteiro.
  try:
    NumberOne = int(input("Por favor, digite um número: "))
    NumberTwo = int(input("Por favor, digite outro número: "))    
  
    Operação = (input("> Qual operação deseja fazer? +, -, *, / : "))

# aqui comecei a fazer as operações selecionadas e mandei mostrar no terminal. usando 'If' e o 'Elif'.
    if Operação == "+":
     print(NumberOne + NumberTwo)
  
    elif Operação == "-":
     print(NumberOne - NumberTwo)

    elif Operação == "*":
     print(NumberOne * NumberTwo)

# aqui coloquei um detalhe importante.  quando o  'user' tentar dividir
# algo pelo número 0, o terminal exibir um erro. também fiz a formatação para dizimas terminar com 3 números depois do ponto.
    elif Operação == "/":
     try:
      operaçãoDiv = NumberOne / NumberTwo
      operaçãoDiv2 = NumberTwo / NumberOne
      print(f'{NumberOne / NumberTwo:.3f}')
     except ZeroDivisionError:
       print("(Oops! Não é possivel dividir por 0. Tente novamente.)") 

# termino do loop inteiro
# msg de erro de caracter       
  except ValueError:
    print("(Oops! Isso não é um número válido. Tente Novamente.)")
 
# estruta de fechar o progama.
  saida = input("Deseja Encerrar? 'S ou N'): ")
  if saida == "S" or saida == "s":
    exit()

  