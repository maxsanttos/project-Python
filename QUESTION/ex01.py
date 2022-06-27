"""
Faça um programa que lei um valor N inteiro e positivo,
Calcule o mostre o valor de E, conforme a Fórme a seguir

e = 1! + 1/1! + 1/2! + 1/3! ... 1/n!
calculo do fatorial

n = int(input("Informe um numero N:"))
fat = 1
i = 1
while i <= n:
    fat *= i
    i += 1
print(f"Resultado da fatorial:{fat} ")



conceito somatorio, ou acomulador

Uma estrutura de repetição p/ acumular os termos do somatorio
variavel acumuladora = E

outra estrutura de repetição para calcula o fatorial

ex: 5! = 5 * 4 * 3 * 2 * 1

aqui no fatorial iremos fazer o produtorio


"""


e = 1
j = 1
while j <= n:
    fat = 1
    i = 1
    while i <= j:
        fat *= i
        i += 1
    e = e + 1/fat
    print(f"Fatorial de N = {j}!")
    print(f"Resultado {fat}\n")
    j += 1
print(f"Resultado {e}")



