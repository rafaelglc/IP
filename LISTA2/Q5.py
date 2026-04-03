print("Radar de Fofocas de Copacabana iniciado!")

rodadas=int(input())
palavra_proibida=""

total_rodadas=rodadas
rodada_atual=0

while rodadas>0:
    pontos=15
    rodadas-=1
    rodada_atual+=1
    numero_fofocas=int(input())
    fofocas_totais=""
    numero_total_fofocas_rodada=numero_fofocas

    while numero_fofocas>0:
        fofoca=input()
        fofocas_totais+=fofoca+" "
        numero_fofocas-=1
    
    palavra_proibida=input()
    lista_fofocas = fofocas_totais.split()

    palavra=""
    palavras_totais=[]

    
    print(f"Rodada {rodada_atual}/{total_rodadas}")
    print(f"Fofocas registradas: {numero_total_fofocas_rodada}")
    print(f"Pontuação inicial: {pontos}")
    
    pontuacao_atual=pontos

    while pontos>0 and palavra!="fim":

        palavra=input()

        if palavra!="fim":

            if palavra in palavras_totais:
                print(f"Você já investigou '{palavra}'. Tente outra.")
        
            else:
                palavras_totais.append(palavra)
                if palavra==palavra_proibida:
                    pontos-=5
                    print(f"Armadilha da Sueli! '{palavra}' era proibida! -5 pontos")

                elif palavra in lista_fofocas:
                    vezes_na_fofoca=lista_fofocas.count(palavra)
                    pontos += vezes_na_fofoca*2

                    print(f"Investigação bem sucedida! '{palavra}' apareceu {vezes_na_fofoca} vez(es).")

                elif palavra not in lista_fofocas:
                    pontos-=1

                    print(f"Nada encontrado sobre '{palavra}'. -1 ponto")

                pontuacao_atual=pontos
                print(f"Pontuação atual: {pontuacao_atual}")
        if pontos<=0:
            print("Você ficou sem pontos! Sueli venceu essa rodada")
        elif palavra=="fim":
            print(f"Rodada encerrada! Pontuação final: {pontuacao_atual}")
        
        