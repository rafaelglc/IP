itens_carol=input()

print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

itens_caminhao=[]

while itens_caminhao!="--":
    itens_caminhao=input()

    if itens_carol in itens_caminhao:
        print("Ótimo, esse caminhão trouxe ['item_recebido1', 'item_recebido2', …]!")
    
    elif itens_carol not in itens_caminhao:
        print("Não encontramos nada que a Carol pediu nesse caminhão.")

    if itens_caminhao not in itens_carol:
        print("Ainda precisamos de ['item_faltante1', 'item_faltante2', …].")

    
if itens_carol in itens_caminhao:
    print("Conseguimos! A Carol ficará muito feliz :)")

else:
    print("Não conseguimos reunir todos os itens que a Carol precisa :(")