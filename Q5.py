sobreviventes=["Kate", "Dwight", "Ada", "Vee"]
assasinos=["Spirit", "Singularidade", "Huntress"]
geradores=0
time_gerador=100
enganchado=0
end_game=False

def mapa(mapa):

    matriz_mapa=[["M" for _ in range(9)] for _ in range(9)]

    matriz_mapa=estruturas(mapa, matriz_mapa)

    return matriz_mapa

def percursos(matriz_mapa, percurso):
    
    percurso_atual=percurso

    d1=matriz_mapa[0][0]
    d2=matriz_mapa[0][8]
    d3=matriz_mapa[8][0]
    d4=matriz_mapa[8][8]

    i=percurso[0]
    j=percurso[1]

    d=matriz_mapa[i+1]
    e=matriz_mapa[i-1]
    c=matriz_mapa[i][j+1]
    b=matriz_mapa[i][j-1]


    Distancia = (matriz_mapa[0] - matriz_mapa[1]) + (matriz_mapa[0][0] - matriz_mapa[0][1])
    vantagem=Distancia*10
    vantagem_incial=60

    return vantagem, vantagem_incial, percurso_atual,d1, d2, d3, d4, d, e, c, b 

def new_percurso(matriz_mapa, movimento, percurso_atual d1, d2, d3, d4, d, e, c, b, vantagem, shack, jungle, lt, time_shack, time_jungle, time_lt, time_M):

    if movimento=="d1":
        percurso_atual=matriz_mapa[0][0]
    elif movimento=="d2":
        percurso_atual=matriz_mapa[0][8]
    elif movimento=="d3":
        percurso_atual=matriz_mapa[8][0]
    elif movimento=="d4":
        percurso_atual=matriz_mapa[8][8]

    i=percurso_atual[0]
    j=percurso_atual[1]
    
    if movimento=="d":
        percurso_atual=matriz_mapa[i+1]
    elif movimento=="e":
        percurso_atual=matriz_mapa[i-1]
    elif movimento=="c":
        percurso_atual=matriz_mapa[j+1]
    elif movimento=="e":
        percurso_atual=matriz_mapa[j-1]





    if percurso_atual==shack:
        vantagem+=time_shack
    elif percurso_atual==jungle:
        vantagem+=time_jungle
    elif percurso_atual==lt:
        vantagem+=time_lt
    else:
        vantagem+=time_M


    return vantagem

def att_geradores(geradores, vantagem, end_game):
    if vantagem>100:
        geradores+=1
        vantagem-=100

    if geradores==5:
        end_game==True

    return geradores, end_game
    
def estruturas(mapa, matriz_mapa):
    time_shack=40
    time_jungle=25
    time_lt=20
    time_M=5

    if mapa=="MecMillan":
        shake=matriz_mapa[5][1]="C"
        jungle=matriz_mapa[3][7]="J"
        lt=matriz_mapa=[1][5]="LT"

    elif mapa=="Autohaven":
        matriz_mapa[1][6]="C"
        matriz_mapa[2][2]="J"
        matriz_mapa[6][3]="LT"

    else:
        matriz_mapa[6][7]="C"
        matriz_mapa[2][2]="J"
        matriz_mapa[7][1]="LT"


    


    return matriz_mapa


print("DBCin x DBIp, que a melhor equipe vença! 🏆")

assasino=""
while assasino not in assasinos:
    assasino=input()
    if assasino in assasinos:
        print("Killer de acordo com o previsto! Boa partida!")

    else:
        print("Killer não previsto! Jogo será atrasado, até que a outra equipe escolha um válido!")

mapa=input()
coordenadas_iniciais=input()


while end_game==False:
    sobrevivente=input()
    percurso=input().split(",")
    movimento=input()