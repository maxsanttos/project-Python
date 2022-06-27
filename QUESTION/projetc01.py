"""
Projeto se refere ao controle 
controle esse que dar o valor que irá pagar na conta de energia em cada bandeira

BANDEIRA

-Verde:Não há nenhum acrescimo no valor nas contas de luz
- Amarela: A cada 100 quilowatts-hora 
consumidos,são adcionado R$1,35 nas faturas.
- Vermelha patamar(1/2):
- Patamar um -> é adcionado o valor de R$ 4,17 a cada 100
quilowatts-hora consumidos.
- Patamar dois -> 
Esse valor sobe para 6,24 em cada 100 quilowatts-hora

""" 




def consumo(leitura):
    anterior = int(input("Porfavor Informe a leitua anterio: "))
    atual = leitura - anterior
    return atual

def calc():
    latual= int(input("Informa a leitura atual: "))
    lanterior = int(input("Informe a leitura anteiror: "))
    fatura = latual - lanterior
    print(f"Seu comsumo é de {fatura} quilowatss")

def gree(atual):
    p = atual * 0.51
    print(f"Parabéns não haverá nenhum acrescimo no valor da sua fatura, Você irá apenas pagar R${p:.2f} reias!")


def yellow(atual):
    x = atual / 100
    x *= 1.35
    print(f"Seu Consumo é {atual} Quilowatss, Sua fatura terá um acrescimo de {x:.2f} reais")
    print(f"entao vacê terá que pagar {(atual * 0.51)+x:.2f} reias")
 

def red1(atual):
        d = atual /100
        d *= 4.17
        print(f"Seu Consumo é {atual} Quilowatss,Sua fatura terá um acrescimo de R${d:.2f} reias")
        print(f"entao vacê terá que pagar {(atual *0.51) + d:.2f} reias")
def red2(atual):
    t = atual /100
    t *= 6.24
    print(f"Seu Consumo é {atual} Quilowatss,Sua fatura terá um acrescimo de R${t:.2f} reias")
    print(f"entao vacê terá que pagar {(atual * 0.51) + t:.2f} reias")
    

       


print("-"*10)
print("Menu")
print("[1] Bandeiras")
print("[2] Calculo do consumo")
print("[0] Sair")
print("-"*10)
opcao = int(input("Escolhar: "))

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



    