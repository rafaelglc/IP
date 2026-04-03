dias=0
moedas_dia=0
moedas_total=0
sinal=""
quantidade_desculpas=0
numero_desculpas=0
desculpa=""
latim=""

print("Ô promessa sem jeito…")
print()

for dia in range(1, 8):

    print(f"Dia {dia}: Quantas moedas João Grilo conseguiu arrecadar hoje?")

    moedas_dia=int(input())
    moedas_total+=moedas_dia
    dias+=1

    print(f"No dia {dia}, o baú já tem R$ {moedas_total}")

print()
print(f"Total arrecadado após o plano: R$ {moedas_total}")
print()

if moedas_total==0:
    print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    print()

    quantidade_desculpas=int(input())

    for numero_desculpa in range(1, quantidade_desculpas+1):
        print(f"Digite a {numero_desculpa}ª desculpa:")
        desculpa=input()
        print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")
    
else:
    print("João Grilo começa a despedida da cachorra:")
    print("'Canis Mortus, Dinherus no Bolsus'")
    print("'Caro nostra quae in patina eius est, canis.'")
    print()
    print("João Grilo, o padeiro acreditou?")
    sinal=input().lower()

    if sinal.lower()=="sim":
        print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
        print("Como o padeiro acreditou?")

    else:
        print("O padeiro não acreditou... João Grilo parte para o Plano B!")

        print()
        print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
        print()

        quantidade_desculpas=int(input())

        for numero_desculpa in range(1, quantidade_desculpas+1):
            print(f"Digite a {numero_desculpa}ª desculpa:")
            desculpa=input()
            print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")


print("Chicó: 'Não sei, só sei que foi assim!'")