"""
Atividade 02 
"""
def mes_do_Ano(dia,mes,ano):
    if mes == 1:
        mes = 'Janeiro'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 2:
        mes = 'Fevereiro'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 3:
        mes = 'Março'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 4:
        mes = 'Abril'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 5:
        mes = 'Maio'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 6:
        mes = 'Junho'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 7:
        mes = 'Julho'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 8:
        mes = 'Agosto'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 9:
        mes = 'Setembro'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 10:
        mes = 'Outubro'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 11:
        mes = 'Novembro'
        print(f"{dia} de {mes} de {ano}")
    elif mes == 12:
        mes = 'Dezembro'
        print(f"{dia} de {mes} de {ano}")

        
dia = int(input("Informe o dia: "))
mes = int(input("Informe o Mês: "))
ano = int(input("Informe o Ano: "))
print(f"{dia}/{mes}/{ano}")

mes_do_Ano(dia,mes,ano)