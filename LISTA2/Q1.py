musicas=""
qtd_musicas=0
nome=""

while nome.lower() != "voa, voa brabuleta":
    nome=input()

    if nome.lower() != "voa, voa brabuleta":
        qtd_musicas +=1

        if musicas=="":
            musicas=nome

        else:
            musicas += " - " + nome

print("Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!")
print(f"A quantidade de músicas selecionadas foi {qtd_musicas}")
print(f"Setlist de músicas: {musicas}")