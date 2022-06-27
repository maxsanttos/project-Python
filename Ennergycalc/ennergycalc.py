
def consumo(leitura):
    anterior = int(input("Porfavor Informe a leitua anterio: "))
    atual = leitura - anterior
    return atual

def calc():
    latual= int(input("Informa a leitura atual: "))
    lanterior = int(input("Informe a leitura anteiror: "))
    c = latual - lanterior
    print(f"Seu comsumo é de {c} quilowatss")

def gree(atual): #Função para o calculo da bandeira verde
    p = atual * 0.51
    print(f"Parabéns não haverá nenhum acrescimo no valor da sua fatura, Você irá apenas pagar R$ {p:.2f} reias!")


def yellow(atual): #Função para o calculo da bandeira amarela
    x = atual / 100
    x *= 1.35
    fatura = (atual * 0.51) + x
    print(f"Seu Consumo é {atual} Quilowatss, Sua fatura terá um acrescimo de {x:.2f} reais")
    print(f"Sua fatura virá com o valor de R$ {fatura:.2f} reias")
 

def red1(atual): #Função para o calculo da bandeira vermelha patamar 01
        d = atual /100
        d *= 4.17
        fatura = (atual * 0.51) + d
        print(f"Seu Consumo é {atual} Quilowatss,Sua fatura terá um acrescimo de R$ {d:.2f} reias")
        print(f"Sua fatura virá com o valor de R$ {fatura:.2f} reias")

def red2(atual): #Função para o calculo da bandeira Vermelha patamar 02
    t = atual /100
    t *= 6.24
    fatura = (atual * 0.51) + t
    print(f"Seu Consumo é {atual} Quilowatss,Sua fatura terá um acrescimo de R$ {t:.2f} reias")
    print(f"Sua fatura virá com o valor de R$ {fatura:.2f} reias")
    

       


print("-"*10)
print("Menu")
print("[1] Bandeiras")
print("[2] Calculo do consumo")
print("[0] Sair")
print("-"*10)
opcao = int(input("\nEscolhar: "))

while opcao != 0:
    if opcao == 1:
        bandeira = int(input("[1]Verde \n[2]Amarelo  \n[3]Vermelho1 \n[4]Vermelho2  \n[0] Sair \n:"))
        if bandeira == 1:
            leitura = int(input("Informe a leitura atual: "))
            gree(consumo(leitura))
        elif bandeira == 2:
            leitura = int(input("Informe a leitura: "))
            yellow(consumo(leitura))
        elif bandeira == 3:
            leitura = int(input("Informe a leitura atual: "))
            red1(consumo(leitura))
        elif bandeira == 4:
            leitura = int(input("Informe a leitura atual: "))
            red2(consumo(leitura))
        elif bandeira == 0:
            print("Saindo")
            break
        else:
            print("Opção inválida!!")
    elif opcao == 2:
        calc()
        break
    else:
        print("Opção inválida!")
        break








