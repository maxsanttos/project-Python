# Pilha de Prato 

prato = 5
pilha = list(range(1,prato+1))
while True:
    print("\nExistem {pilha}pratos na pilha")
    print("Pilha atual: ",pilha)
    print("Digite E para empilhar um novo prato")
    print("ou D para desempilhar, S para sair.")
    operacao = input("Operação(E,D,S)").upper()
    print(operacao)
    if operacao == 'D':
        if(len(pilha)):
            lavado = pilha.pop(-1)
            print("Prato:{lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar")
    elif operacao == 'E':
        prato +=1 #Novo prato
    elif operacao == 'S':
        print("Até mais!!")
        break
    else:
         print("Operação inválida! Digite apenas E,D ou S !")
        
        
        
