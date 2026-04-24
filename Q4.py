Sefiras=["Malkuth", "Yesod", "Binah"]

def Dias(quantidade_de_dias):

    while quantidade_de_dias>0:
        dia=0
        energianecessaria=100

        print(f"Angela: Hoje é o dia {dia} de {quantidade_de_dias}. Espero mais um expediente concluído com excelência.")
        
        sefirot=input()
        
        if sefirot in Sefiras:
            if sefirot=="Malkuth":
                print("Hoje é o dia da Malkuth!")
                print("Malkuth: Ah, onde estão meus modos! Malkuth se apresentando!")
                print("Malkuth: Estamos responsáveis hoje por organizar por tamanho nossa lista de funcionários do time de controle, vamos entregar com resultados perfeitos!")
                print()

                nomes=input().split(" ")

                if nomes!=[]:

                    for repeticao in range(len(nomes)-1):
                        for i in range(len(nomes)-1):
                            j=i+1
                            if len(nomes[i])>len(nomes[j]):
                                nomes[i], nomes[j]=nomes[j], nomes[i]

                    energia=(len(nomes[0])+len(nomes[-1]))*20

                    print(nomes)

                    print(f"Energia Coletada: {energia} / {energianecessaria}")

                    if energia>=energianecessaria:
                        print("Malkuth: O treino vespertino de hoje foi um sucesso! Estarei esperando vocês no período noturno, pessoal!")
                        print()

                    else:
                        print("Malkuth: Ah não.. não conseguimos energia suficiente... amanhã eu dobrarei a carga horária para que a gente possa concluir o expediente com excelência!")
                        print()
                
                else:
                    print("Malkuth: Pessoal?! Onde está todo mundo?! Isso é inaceitável!")
                    print()

            elif sefirot=="Yesod":
                print("Hoje é dia do Yesod!")
                print("Yesod: Você é a cabeça dessa corporação, você deve agir como um exemplo para os outros e fazer certeza que esse dia passe coordialmente seguindo as regras.")
                print("Yesod: Hoje estamos com um problema a resolver. Você é um progamador, não é? Hoje recebemos vários caracteres, e você terá de as comprimir para facilitar as informações.")
                print()

                sequencia=input()
                i=0
                notascomprimidas=""

                while i<len(sequencia) and sequencia[i]!="&":
                    letra_atual=sequencia[i]
                    contagem=1

                    while i+1<len(sequencia) and sequencia[i+1]==letra_atual:
                        contagem+=1
                        i+=1
                    
                    if contagem>1:
                        notascomprimidas+=str(contagem)+letra_atual

                    else:
                        notascomprimidas+=letra_atual

                    i+=1

                if "&" not in sequencia:
                    print(f"Yesod: Aqui está a lista de caracteres comprimidos: '{notascomprimidas}'")
                    print()

                else:
                    print("Yesod: Os caracteres de hoje estavam corrompidas... devemos encerrar o dia mais cedo e investigar.")
                    print(f"Yesod: Pelo menos, essas informações ainda estão conosco: '{notascomprimidas}'")
                    print()
                
                
            elif sefirot=="Binah":
                print("Hoje é o dia da Binah.")
                print("Binah: ...Você chegou.")
                print("Binah: Você já deve saber o que fazer. Espero um bom resultado vindo de você.")
                print()

        else:
            print("Angela: Essa sefirot não está disponível hoje.")
            print()

        dia+=1
        quantidade_de_dias-=1
        consumo_energia+=40



def Malkuth_ordenacao():

def Yesod_compressao():

def Binah_matrizes():


quantidade_de_dias=int(input())

print("Hoje é o dia da Lobotomy CinCorporation!")
print()

