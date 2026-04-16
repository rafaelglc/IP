objetivos_missao=["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
itens_bonus=["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixos=["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]
resto=[]
inventario=[]
pontos=0
objetivos_encontrados=[]
itens_encontrados=[]


coleta=""

#FASE 1

print("FASE 1:")
print("Marty McFly: Vamos buscar os Recursos que o Doc pediu.")

#ARMAZENAMENTO

while coleta!="Fim Da Coleta!":
    coleta=input()
    
    if coleta not in objetivos_missao and coleta not in itens_bonus and coleta not in lixos:
        resto.join(coleta)
        inventario.join(coleta)

    if coleta not in lixos:
        inventario.join(coleta)

    if coleta in objetivos_missao:
        objetivos_encontrados.join(coleta)
    elif coleta in itens_bonus:
        itens_encontrados.join(coleta)

    if coleta not in objetivos_encontrados and coleta in objetivos_missao:
        print("Marty McFly: Boa Embananado, estávamos precisando disso.")
    elif coleta in objetivos_encontrados:
        print("Marty McFly: Por via das dúvidas, vamos levar mais.")
    
    if coleta in lixos:
        print("Marty McFly: Pra que eu preciso disso? Só vai encher meu inventário.")
    elif coleta in itens_bonus:
        print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")

print("Marty McFly: Nossa coleta termina aqui.")
#ORDENACAO


#PONTUACAO

for item in inventario:
    if item in objetivos_missao:
        pontos+=30
        coleta_objetivo=True

    elif item in itens_bonus:
        pontos+=10
        
    elif item in lixos:
        pontos-=5

    if pontos>100:
        pontos=100
    elif pontos<0:
        pontos=0

if coleta_objetivo==False:
    print("Marty McFly: Infelizmente não encontramos nenhum dos objetivos, não poderemos continuar com a missão.")

else:
    print(f"PONTUAÇÃO DA COLETA = {pontos}")
    if pontos<30:
        print("Marty McFly: Pontuação Insuficiente, não poderemos continuar com a missão.")
    
    else:

        print("acabou")