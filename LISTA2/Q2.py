dinheiro_inicial=int(input())
compra=""
qtd_compras=0
custo=int()
custo_total=0
modelo=""



while compra.lower() !="amauri":
    compra=input()
    custo=int(input())
    if compra.lower() !="amauri":
        custo=int(input())

        qtd_compras+=1
        custo_total+=custo

        if compra.lower()=="carro":
            modelo.lower()==input()


print(f"A família possui {dinheiro_inicial} ainda, talvez ele fique tranquilo hoje")
if compra=="Amauri":
    print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")

if custo>500000:
    print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")

elif custo<1000:
    print(f'1Será que se acalmaram?! {compra} por "somente" {custo} reais')

else:
    print(f"Gastaram {custo} reais para comprar um(a) {compra}")

if compra=="carro":
    if modelo.lower()=="chevette":
        print("chevette : Relembrando as origens será?")
    elif modelo.lower()=="Jeep":
        print("jeep : Será que ele tá se preparando para outra aventura que não irá?")
    elif modelo.lower()=="bmw":
        print("bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁")

print(f"{qtd_compras} - {custo_total} reais")