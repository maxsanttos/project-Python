l = [7,9,10,12]
p = int(input("Digite um número a pesquisar: "))
for e in l:
    if e == p:
        print("Elemento encontrado :) !")
        break
else:
    print("Elemento não encontrado :( ")

    