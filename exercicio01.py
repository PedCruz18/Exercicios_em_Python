# Aqui aprendi sobre o ''while'' e iniciei o laço do loop caso o 'user' quiser continuar o progama.
while True:

 # aqui é o nome do progaminha.
 print("VERIFICAÇÃO DE IDADE PARA VOTAR:")
 
# Aqui estou perguntando ao 'user' qual é a idade dele.
 IdadeUser = int(input("Qual é a sua Idade? >> "))
 
# Aqui estou comparando a idade ao número minimo requerido. 
 if IdadeUser >= 16:
    print(">> você PODE votar :)")
 else:
    print(">> você NÃO pode votar :(")

# aqui estou retomando o laço do while e perguntando se o 'user' deseja continuar ou não o progaminha.
 saida = input(">> Deseja Encerrar? 'S ou N' > ")
 
 if saida == "S":
    break
 if saida == "s":
     break