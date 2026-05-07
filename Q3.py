def movimentos(caminho, resistencia, total_itens):
    if resistencia<=0:
        print("A correnteza está muito forte... não consigo continuar.")
        print("O príncipe afundou... Úrsula venceu desta vez.")
        return
    elif caminho=="":
        print(f"Eric foi salvo! E Ariel ainda guardou {total_itens} bugigangas na sua gruta.")
        return
    else:
        novo_caminho=caminho[1:]
        movimento_atual=novo_caminho[0]
        resistencia-=1

        if movimento_atual=="Linguado":
            print("Obrigada, Linguado! Vamos rápido!")
            return movimentos(novo_caminho, resistencia+2, total_itens)
        elif movimento_atual=="Polvo":
            print("Cuidado com os servos da bruxa!")
            return movimentos(novo_caminho, resistencia-2, total_itens)
        elif movimento_atual=="~":
            return movimentos(novo_caminho, resistencia, total_itens)
        else:
            valor_bugiganga=int(movimento_atual)
            total_itens+=valor_bugiganga
            return movimentos(novo_caminho, resistencia, total_itens)
        

caminho=input().split(" ")
resistencia=6
total_itens=0
movimentos(caminho, resistencia, total_itens)