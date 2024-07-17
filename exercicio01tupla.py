#Exer.: 1
print("\n")
print("Crie uma tupla chamada minha_tupla que armazene as cores do arco-íris e Exiba na tela a cor que está na quarta posição da tupla.")

tupla_multipla = ("vermelho", "laranja", "amarelo", "verde", "azul", "anil", "violeta" )
print(tupla_multipla[3])

print("-------------------------------------------------")
print("\n")
#----------------------------------------
print("\n")
print("Tente modificar o valor da cor na quinta posição da tupla. (Isso deve gerar um erro, pois tuplas são imutáveis).")

#Erro---------------------------------------------
#tupla_multipla[4] = input("Adicione o valor: ")
#Solução------------------------------------------
convertlista = list(tupla_multipla)
convertlista[5] = input("Qual valor deseja adicionar?: ")
tupla_multipla_atualizada = tuple(convertlista)
print(tupla_multipla_atualizada)

print("-------------------------------------------------")
print("\n")
#----------------------------------------
print("reverso")

tupla_multipla_inversa = tupla_multipla[::-1]
print(tupla_multipla_inversa)
