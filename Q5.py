sobreviventes=["Kate", "Dwight", "Ada", "Vee"]
ganchos_sobreviventes=[0, 0, 0, 0]
total_ganchos=0
assasinos=["Spirit", "Singularidade", "Huntress"]
geradores=0
time_gerador=100

end_game=False

def Mapa(mapa):

    matriz_mapa=[["M" for _ in range(9)] for _ in range(9)]

    matriz_mapa=estruturas(mapa, matriz_mapa)

    return matriz_mapa

def percursos(matriz_mapa, coordenadas_iniciais, new_linha, maior_dist):
    
    
    linha_atual=coordenadas_iniciais[0]
    coluna_atual=coordenadas_iniciais[1]


    if new_linha < 0 or new_linha > 8:
        print("❌ Travou na parede! Deixou fácil pro killer!")


    Distancia = (matriz_mapa[0] - matriz_mapa[1]) + (matriz_mapa[0][0] - matriz_mapa[0][1])
    vantagem=maior_dist*10
    vantagem_incial=60

    return vantagem, vantagem_incial, matriz_mapa, linha_atual, coluna_atual

def new_percurso(movimento, percurso_atual, linha_atual, coluna_atual, vantagem):

    new_linha, new_coluna= linha_atual, coluna_atual

    if movimento=="d1":
        new_linha -= 1; new_coluna -= 1
    elif movimento=="d2":
        new_linha -= 1; new_coluna += 1
    elif movimento=="d3":
        new_linha += 1; new_coluna -= 1
    elif movimento=="d4":
        new_linha += 1; new_coluna += 1

    
    if movimento=="d":
        new_coluna += 1
    elif movimento=="e":
        new_coluna -= 1
    elif movimento=="c":
        new_linha -= 1
    elif movimento=="b":
        new_linha += 1

    return new_coluna, new_linha

def att_geradores(geradores, time_acumulado, end_game):
    while time_acumulado>100 and geradores<5:
        geradores+=1
        time_acumulado-=100

    if geradores==5:
        end_game==True

    return geradores, time_acumulado, end_game
    
def estruturas(matriz_mapa, linha, coluna):
    estrutura=matriz_mapa[linha][coluna]

    if estrutura=="C":
        time=40
        matriz_mapa[linha][coluna]="M"
        print("🏃 Usou a Shack!")

    elif estrutura=="J":
        time=25
        matriz_mapa[linha][coluna]="M"
        print("🏃 Usou a Jungle!")

    elif estrutura=="LT":
        time_lt=20
        print("🏃 Usou a LT!")
    
    else:
        time=5
        print("🌿 Correu pelo mapa.")

    return time


print("DBCin x DBIp, que a melhor equipe vença! 🏆")

assasino=""
while assasino not in assasinos:
    assasino=input()
    if assasino in assasinos:
        print("Killer de acordo com o previsto! Boa partida!")

    else:
        print("Killer não previsto! Jogo será atrasado, até que a outra equipe escolha um válido!")

mapa=input()
coordenadas_iniciais=input().split(",")
linha_inicial=int(coordenadas_iniciais[0])
coluna_inicial=int(coordenadas_iniciais[1])

distancia_assasino_d1=abs(linha_inicial-0)+abs(coluna_inicial-0)
distancia_assasino_d2=abs(linha_inicial-0)+abs(coluna_inicial-8)
distancia_assasino_d3=abs(linha_inicial-8)+abs(coluna_inicial-0)
distancia_assasino_d4=abs(linha_inicial-8)+abs(coluna_inicial-8)

maior_dist=max(distancia_assasino_d1, distancia_assasino_d2, distancia_assasino_d3, distancia_assasino_d4)

matriz_mapa=Mapa(mapa)

if maior_dist==distancia_assasino_d1:
    linha_killer, coluna_killer = 0, 0
    spawn_assasino=matriz_mapa[0][0]
    print(f"O(A) {assasino} nasceu na posição {linha_killer}, {coluna_killer}.")
    print("A vossa vantagem inicial de distância é de {distancia} espaços!")

elif maior_dist==distancia_assasino_d2:
    linha_killer, coluna_killer = 0, 8
    spawn_assasino=matriz_mapa[0][8]
    print(f"O(A) {assasino} nasceu na posição [{linha_killer}, {coluna_killer}].")
    print("A vossa vantagem inicial de distância é de {distancia} espaços!")

elif maior_dist==distancia_assasino_d3:
    linha_killer, coluna_killer = 8, 0
    spawn_assasino=matriz_mapa[8][0]
    print(f"O(A) {assasino} nasceu na posição [{linha_killer}, {coluna_killer}].")
    print("A vossa vantagem inicial de distância é de {distancia} espaços!")

elif maior_dist==distancia_assasino_d4:
    linha_killer, coluna_killer = 8, 8
    spawn_assasino=matriz_mapa[8][8]
    print(f"O(A) {assasino} nasceu na posição [{linha_killer}, {coluna_killer}].")
    print("A vossa vantagem inicial de distância é de {distancia} espaços!")


while end_game==False:
    print(f"--- STATUS: {geradores}/5 Geradores | {total_ganchos}/12 Ganchos ---")

    sobrevivente=input()
    if sobrevivente not in sobreviventes:
        print("⚠️ Personagem não pertence à equipe!")
        print("Esse personagem não está previsto na sua equipe ou já tem 2 ganchos.")
    else:
        indice=sobreviventes.index(sobrevivente)
        quantidade_ganchos=ganchos_sobreviventes[indice]

        if quantidade_ganchos>2:
            print(f"⚠️ O/A {sobrevivente} já tem 2 ganchos!")
            print("Esse personagem não está previsto na sua equipe ou já tem 2 ganchos.")
        else:
            
            movimento=input()
            passos=movimento.split(", ")

            fugindo=True
            linha_atual=linha_inicial
            coluna_atual=coluna_inicial

            for i in passos:
                if fugindo==True:
                    new_coluna, new_linha=new_percurso()

                    if 0 > new_coluna or new_coluna > 8 or 0 > new_linha or new_linha>8:
                        print("❌ Travou na parede! Deixou fácil pro killer!")
                        fugindo=False
                    
                    else:
                        linha_atual, coluna_atual=new_linha, new_coluna
                        vantagem+=estruturas(matriz_mapa, linha_atual, coluna_atual)

    geradores+=att_geradores(geradores, time_acumulado, end_game)