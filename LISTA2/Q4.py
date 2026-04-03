print("Avenida Brasil: A Vingança de Nina!")

#variaveis:
pendrives=int(input())
numero_atual_pendrive=0
total_pendrives=pendrives
pendrives_abertos=0

while numero_atual_pendrive<total_pendrives:
    numero_atual_pendrive+=1
    senha=input()

    print(f"Descriptografando pendrive {numero_atual_pendrive} de {total_pendrives}...")

    quantidade_letras_senha=0

    #CONTADOR DAS LETRAS DA SENHA:
    for letra in senha:
        if letra != " ":
            quantidade_letras_senha+=1

    tentativas=quantidade_letras_senha*2
    estado_atual_da_senha=""

    for letra in senha:
        if letra == " ":
            estado_atual_da_senha+=" "
        else:
            estado_atual_da_senha+="_"

    vitoria=False
    letras_utilizadas=""

    #TENTATIVAS PARA DESCOBRIR A SENHA:

    while tentativas>0 and vitoria==False:
        letra_tentada=input()
        tentativas-=1
        
        if letra_tentada in letras_utilizadas:
            print("Max: Ele já tentou isso, Carminha...")

        else:
            letras_utilizadas+=letra_tentada
            novo_estado_da_senha=""
            correta=False

            for i in range(len(senha)):
                if senha[i] == letra_tentada:
                    novo_estado_da_senha+=letra_tentada
                    correta=True
                else:
                    novo_estado_da_senha+=estado_atual_da_senha[i]

            #INEDITA:
            if correta:
                print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")

            else:
                print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")

            estado_atual_da_senha=novo_estado_da_senha

        print(f"Senha: {estado_atual_da_senha}")

        if "_" not in estado_atual_da_senha and tentativas>=0:
            vitoria=True
            print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {numero_atual_pendrive} está aberto.")
            pendrives_abertos+=1
            
    if not vitoria:
        print(f"Carminha: Consegui! As fotos do pendrive {numero_atual_pendrive} estão a salvo comigo.")


print(f"Conseguimos abrir {pendrives_abertos} de {total_pendrives} pendrives!")

if total_pendrives>0:
    taxa_T=(pendrives_abertos/total_pendrives)*100

    if taxa_T==0:
        print("Tufão continuará sendo enganado para sempre...")
    elif taxa_T>0 and taxa_T<=50:
        print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")
    elif taxa_T>50 and taxa_T<100:
        print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")
    elif taxa_T==100:
        print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.")
