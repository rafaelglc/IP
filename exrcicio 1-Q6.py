robin_disponibilidade=input().capitalize()
estelar_disponibilidade=input().capitalize()
ciborgue_disponibilidade=input().capitalize()
ravena_disponibilidade=input().capitalize()
mutano_disponibilidade=input().capitalize()
quantidade_candidatos=0
candidatos=""
selecionado=""

#quantidade candidatos

if robin_disponibilidade == "S":
    quantidade_candidatos+=1
    candidatos+="Robin"

if estelar_disponibilidade == "S":
    quantidade_candidatos+=1
    candidatos+="Estelar"

if ciborgue_disponibilidade == "S":
    quantidade_candidatos+=1
    candidatos+="Ciborgue"

if ravena_disponibilidade == "S":
    quantidade_candidatos+=1
    candidatos+="Ravena"
if mutano_disponibilidade == "S":
    quantidade_candidatos+=1
    candidatos+="Mutano"


#casos especificos

if quantidade_candidatos==2:
    if "Robin" in candidatos and "Estelar" in candidatos:
        selecionado =="Estelar"
    elif "Ravena" in candidatos and "Mutano" in candidatos:
        selecionado =="Ravena"
    elif "Ciborgue" in candidatos and "Mutano" in candidatos:
        quantidade_mutano=int(input())
        quantidade_ciborgue=int(input())


if quantidade_candidatos>2 and quantidade_candidatos<=4:
    if "Robin" in candidatos:
        selecionado=="Robin"
    else:
        selecionado=="Ravena"

if quantidade_candidatos==5:







if quantidade_candidatos==2:
    if (robin_disponibilidade == "S" and estelar_disponibilidade =="S") or (mutano_disponibilidade == "S" and ravena_disponibilidade == "S"):
        print("Parece que o cavalherismo ainda não morreu não é mesmo?")














if quantidade_candidatos==0:
    print("Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!")

elif quantidade_candidatos==1:
    print("Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!")

elif quantidade_candidatos >2 and quantidade_candidatos<=4:
    print(f"Mesmo com {quantidade_candidatos} candidatos, o(a) {selecionado} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {selecionado}!")

elif quantidade_candidatos==5:
    print("Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!")