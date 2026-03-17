#MAQUINA 1

nome_maquina1=input()
quantidade_pecas1=int(input())
reacao_candace1=input()
letras_maquina1=len(nome_maquina1)
pontuacao1=letras_maquina1+quantidade_pecas1
limite_pecas=25
limite_nome=15
desempate_1=0
desempate_2=0
desempate_3=0
desempate_4=0

#PONTUACAO MAQUINA 1

#REACAO CANDACE

if reacao_candace1 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao1=pontuacao1+30
elif reacao_candace1 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao1=pontuacao1+20
elif reacao_candace1 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao1=pontuacao1+10
elif reacao_candace1 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao1=pontuacao1+0
elif reacao_candace1 == "SÉRIO? SÓ ISSO?":
    pontuacao1=pontuacao1-5
elif reacao_candace1 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao1=pontuacao1-10
elif reacao_candace1 == "AH, ESQUECE…":
    pontuacao1=pontuacao1-15

if "i" in nome_maquina1 and "n" in nome_maquina1 and "a" in nome_maquina1 and "t" in nome_maquina1 and "o" in nome_maquina1 and "r" in nome_maquina1:
    pontuacao1=pontuacao1-50
elif "P" in nome_maquina1 and "e" in nome_maquina1 and "r" in nome_maquina1  and "y" in nome_maquina1:
    pontuacao1=pontuacao1+20

#NOME DA MÁQUINA

if nome_maquina1 == "HidromassagemAutomáticaDoPerry":
    pontuacao1=pontuacao1*2
elif nome_maquina1 == "MáquinaDeBanhoForçado":
    pontuacao1=pontuacao1-20
elif "i" in nome_maquina1 and "n" in nome_maquina1 and "a" in nome_maquina1 and "t" in nome_maquina1 and "o" in nome_maquina1 and "r" in nome_maquina1:
    pontuacao1=pontuacao1-50
elif "p" in nome_maquina1 and "e" in nome_maquina1 and "r" in nome_maquina1  and "y" in nome_maquina1:
    pontuacao1=pontuacao1+20

#MAQUINA 2

nome_maquina2=input()
quantidade_pecas2=int(input())
reacao_candace2=input()
letras_maquina2=len(nome_maquina2)
pontuacao2=letras_maquina2+quantidade_pecas2

#PONTUACAO MAQUINA 2

#REACAO CANDACE 2

if reacao_candace2 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao2=pontuacao2+30
elif reacao_candace2 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao2=pontuacao2+20
elif reacao_candace2 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao2=pontuacao2+10
elif reacao_candace2 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao2=pontuacao2+0
elif reacao_candace2 == "SÉRIO? SÓ ISSO?":
    pontuacao2=pontuacao2-5
elif reacao_candace2 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao2=pontuacao2-10
elif reacao_candace2 == "AH, ESQUECE…":
    pontuacao2=pontuacao2-15

if "i" in nome_maquina2 and "n" in nome_maquina2 and "a" in nome_maquina2 and "t" in nome_maquina2 and "o" in nome_maquina2 and "r" in nome_maquina2:
    pontuacao2=pontuacao2-50
elif "p" in nome_maquina2 and "e" in nome_maquina2 and "r" in nome_maquina2  and "y" in nome_maquina2:
    pontuacao2=pontuacao2+20    
#NOME DA MÁQUINA 2

if nome_maquina2 == "HidromassagemAutomáticaDoPerry":
    pontuacao2=pontuacao2*2
elif nome_maquina2 == "MáquinaDeBanhoForçado":
    pontuacao2=pontuacao2-20


#MAQUINA 3

nome_maquina3=input()
quantidade_pecas3=int(input())
reacao_candace3=input()
letras_maquina3=len(nome_maquina3)
pontuacao3=letras_maquina3+quantidade_pecas3

#PONTUACAO MAQUINA 3

#REACAO CANDACE 3

if reacao_candace3 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao3=pontuacao3+30
elif reacao_candace3 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao3=pontuacao3+20
elif reacao_candace3 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao3=pontuacao3+10
elif reacao_candace3 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao3=pontuacao3+0
elif reacao_candace3 == "SÉRIO? SÓ ISSO?":
    pontuacao3=pontuacao3-5
elif reacao_candace3 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao3=pontuacao3-10
elif reacao_candace3 == "AH, ESQUECE…":
    pontuacao3=pontuacao3-15


elif "i" in nome_maquina3 and "n" in nome_maquina3 and "a" in nome_maquina3 and "t" in nome_maquina3 and "o" in nome_maquina3 and "r" in nome_maquina3:
    pontuacao3=pontuacao3-50
elif "p" in nome_maquina3 and "e" in nome_maquina3 and "r" in nome_maquina3  and "y" in nome_maquina3:
    pontuacao3=pontuacao3+20

#NOME DA MÁQUINA 3

if nome_maquina3 == "HidromassagemAutomáticaDoPerry":
    pontuacao3=pontuacao3*2
elif nome_maquina3 == "MáquinaDeBanhoForçado":
    pontuacao3=pontuacao3-20


#MAQUINA 4

nome_maquina4=input()
quantidade_pecas4=int(input())
reacao_candace4=input()
letras_maquina4=len(nome_maquina4)
pontuacao4=letras_maquina4+quantidade_pecas4

#PONTUACAO MAQUINA 4

#REACAO CANDACE 4

if reacao_candace4 == "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!":
    pontuacao4=pontuacao4+30
elif reacao_candace4 == "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!":
    pontuacao4=pontuacao4+20
elif reacao_candace4 == "OK... ISSO É BEM ESTRANHO.":
    pontuacao4=pontuacao4+10
elif reacao_candace4 == "AH, NEM É TÃO IMPRESSIONANTE ASSIM.":
    pontuacao4=pontuacao4+0
elif reacao_candace4 == "SÉRIO? SÓ ISSO?":
    pontuacao4=pontuacao4-5
elif reacao_candace4 == "MÃE! A MÁQUINA SUMIU DE NOVO!":
    pontuacao4=pontuacao4-10
elif reacao_candace4 == "AH, ESQUECE…":
    pontuacao4=pontuacao4-15

if "i" in nome_maquina4 and "n" in nome_maquina4 and "a" in nome_maquina4 and "t" in nome_maquina4 and "o" in nome_maquina4 and "r" in nome_maquina4:
    pontuacao4=pontuacao4-50
elif "p" in nome_maquina4 and "e" in nome_maquina4 and "r" in nome_maquina4  and "y" in nome_maquina4:
    pontuacao4=pontuacao4+20

#NOME DA MÁQUINA 4

if nome_maquina4 == "HidromassagemAutomáticaDoPerry":
    pontuacao4=pontuacao4*2
elif nome_maquina4 == "MáquinaDeBanhoForçado":
    pontuacao4=pontuacao4-20


vencedor=nome_maquina1
P_vencedor=pontuacao1
vice=nome_maquina2
P_vice=pontuacao2
terceiro=nome_maquina3
P_terceiro=pontuacao3
quarto=nome_maquina4
P_quarto=pontuacao4

if (P_vencedor<P_vice):
    P_vencedor, P_vice = P_vice, P_vencedor
    vencedor, vice = vice, vencedor
elif (P_vencedor==P_vice):

    #DESEMPATE LETRAS
    if letras_maquina1>limite_nome:
        desempate_1+=1
    else:
        desempate_1==0
    
    if letras_maquina2>limite_nome:
        desempate_2+=1
    else:
        desempate_2==0
    
    #DESEMPATE PEÇAS
    if quantidade_pecas1>limite_pecas:
        desempate_1+=1
    else:
        desempate_1==0
    
    if quantidade_pecas2>limite_pecas:
        desempate_2+=1
    else:
        desempate_2==0
    
    #RESOLUÇÃO DO DESEMPATE
    if desempate_1>desempate_2:
        P_vencedor>P_vice
    elif desempate_1<desempate_2:
        P_vencedor<P_vice
    elif desempate_1==desempate_2:
        P_vencedor==P_vice

        #DESEMPATE POR PECAS
        if quantidade_pecas1>quantidade_pecas2:
            P_vencedor>P_vice
        elif quantidade_pecas1<quantidade_pecas2:
            P_vencedor<P_vice
        elif quantidade_pecas1==quantidade_pecas2:
            P_vencedor==P_vice

            #DESEMPATE POR LETRAS
            if letras_maquina1>letras_maquina2:
                P_vencedor>P_vice
            elif letras_maquina1<letras_maquina2:
                P_vencedor<P_vice


if (P_vencedor<P_terceiro):
    P_vencedor, P_terceiro = P_terceiro, P_vencedor
    vencedor, terceiro = terceiro, vencedor
elif (P_vencedor==P_terceiro):
    if letras_maquina1>limite_nome:
        desempate_1+=1
    else:
        desempate_1==0
    if letras_maquina3>limite_nome:
        desempate_3+=1
    else:
        desempate_3==0
    if quantidade_pecas1>limite_pecas:
        desempate_1+=1
    else:
        desempate_1==0
    if quantidade_pecas3>limite_pecas:
        desempate_3+=1
    else:
        desempate_3==0
    if desempate_1>desempate_3:
        P_vencedor>P_terceiro
    elif desempate_1<desempate_3:
        P_vencedor<P_terceiro
    elif desempate_1==desempate_3:
        P_vencedor==P_terceiro
        if quantidade_pecas1>quantidade_pecas3:
            P_vencedor>P_terceiro
        elif quantidade_pecas1<quantidade_pecas3:
            P_vencedor<P_terceiro
        elif quantidade_pecas1==quantidade_pecas3:
            P_vencedor==P_terceiro
            if letras_maquina1>letras_maquina3:
                P_vencedor>P_terceiro
            elif letras_maquina1<letras_maquina3:
                P_vencedor<P_terceiro


if (P_vencedor<P_quarto):
    P_vencedor, P_quarto = P_quarto, P_vencedor
    vencedor, quarto = quarto, vencedor
elif (P_vencedor==P_quarto):
    if letras_maquina1>limite_nome:
        desempate_1+=1
    else:
        desempate_1==0
    if letras_maquina4>limite_nome:
        desempate_4+=1
    else:
        desempate_4==0
    if quantidade_pecas1>limite_pecas:
        desempate_1+=1
    else:
        desempate_1==0
    if quantidade_pecas4>limite_pecas:
        desempate_4+=1
    else:
        desempate_4==0
    if desempate_1>desempate_4:
        P_vencedor>P_quarto
    elif desempate_1<desempate_4:
        P_vencedor<P_quarto
    elif desempate_1==desempate_4:
        P_vencedor==P_quarto
        if quantidade_pecas1>quantidade_pecas4:
            P_vencedor>P_quarto
        elif quantidade_pecas1<quantidade_pecas4:
            P_vencedor<P_quarto
        elif quantidade_pecas1==quantidade_pecas4:
            P_vencedor==P_quarto
            if letras_maquina1>letras_maquina4:
                P_vencedor>P_quarto
            elif letras_maquina1<letras_maquina4:
                P_vencedor<P_quarto


if (P_vice<P_terceiro):
    P_vice, P_terceiro = P_terceiro, P_vice
    vice, terceiro = terceiro, vice
elif (P_vice==P_terceiro):
        if letras_maquina2>limite_nome:
            desempate_2+=1
        else:
            desempate_2==0
        if letras_maquina3>limite_nome:
            desempate_3+=1
        else:
            desempate_3==0
        if quantidade_pecas2>limite_pecas:
            desempate_2+=1
        else:
            desempate_2==0
        if quantidade_pecas3>limite_pecas:
            desempate_3+=1
        else:
            desempate_3==0
        if desempate_2>desempate_3:
            P_vice>P_terceiro
        elif desempate_2<desempate_3:
            P_vice<P_terceiro
        elif desempate_2==desempate_3:
            P_vice==P_terceiro
            if quantidade_pecas2>quantidade_pecas3:
                P_vice>P_terceiro
            elif quantidade_pecas2<quantidade_pecas3:
                P_vice<P_terceiro
            elif quantidade_pecas2==quantidade_pecas3:
                P_vice==P_terceiro
                if letras_maquina2>letras_maquina3:
                    P_vice>P_terceiro
                elif letras_maquina2<letras_maquina3:
                    P_vice<P_terceiro

if (P_vice<P_quarto):
    P_vice, P_quarto = P_quarto, P_vice
    vice, quarto = quarto, vice
elif (P_vice==P_quarto):
        if letras_maquina2>limite_nome:
            desempate_2+=1
        else:
            desempate_2==0
        if letras_maquina4>limite_nome:
            desempate_4+=1
        else:
            desempate_4==0
        if quantidade_pecas2>limite_pecas:
            desempate_2+=1
        else:
            desempate_2==0
        if quantidade_pecas4>limite_pecas:
            desempate_4+=1
        else:
            desempate_4==0
        if desempate_2>desempate_4:
            P_vice>P_quarto
        elif desempate_2<desempate_4:
            P_vice<P_quarto
        elif desempate_2==desempate_4:
            P_vice==P_quarto
            if quantidade_pecas2>quantidade_pecas4:
                P_vice>P_quarto
            elif quantidade_pecas2<quantidade_pecas4:
                P_vice<P_quarto
            elif quantidade_pecas2==quantidade_pecas4:
                P_vice==P_quarto
                if letras_maquina2>letras_maquina4:
                    P_vice>P_quarto
                elif letras_maquina2<letras_maquina4:
                    P_vice<P_quarto


if (P_terceiro<P_quarto):
    P_terceiro, P_quarto = P_quarto, P_terceiro
    terceiro, quarto = quarto, terceiro
elif (P_terceiro==P_quarto):
        if letras_maquina3>limite_nome:
            desempate_3+=1
        else:
            desempate_3==0
        if letras_maquina4>limite_nome:
            desempate_4+=1
        else:
            desempate_4==0
        if quantidade_pecas3>limite_pecas:
            desempate_3+=1
        else:
            desempate_3==0
        if quantidade_pecas4>limite_pecas:
            desempate_4+=1
        else:
            desempate_4==0
        if desempate_3>desempate_4:
            P_terceiro>P_quarto
        elif desempate_3<desempate_4:
            P_terceiro<P_quarto
        elif desempate_3==desempate_4:
            P_terceiro==P_quarto
            if quantidade_pecas3>quantidade_pecas4:
                P_terceiro>P_quarto
            elif quantidade_pecas3<quantidade_pecas4:
                P_terceiro<P_quarto
            elif quantidade_pecas3==quantidade_pecas4:
                P_terceiro==P_quarto
                if letras_maquina3>letras_maquina4:
                    P_terceiro>P_quarto
                elif letras_maquina3<letras_maquina4:
                    P_terceiro<P_quarto

#RANKING FINAL

print(f"1º lugar - {vencedor} : {P_vencedor} pontos")
print(f"2º lugar - {vice} : {P_vice} pontos")
print(f"3º lugar - {terceiro} : {P_terceiro} pontos")
print(f"4º lugar - {quarto} : {P_quarto} pontos")