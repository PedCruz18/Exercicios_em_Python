print("\n")
frutas = ("banana", "maçã", "laranja")
legumes = ("tomate", "cenoura", "batata")
mercado = frutas + legumes
print("Seu Estoque: " f'{mercado}')

escolha_frut = input("Qual fruta deseja verificar no estoque de frutas?: ")
if escolha_frut == "laranja":
    if "laranja" in frutas:
     print("Laranja está presente.")
else:
     print("o item está em falta.")
print("\n")

escolha_leg = input("Qual legume deseja verificar no estoque de legumes?: ")
if escolha_frut == "alface":
    if "alface" in legumes:
     print("Alface está presente.")
else:
     print("o item está em falta.")