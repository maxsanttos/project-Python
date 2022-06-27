

qtd = int(input("Quantas vezes esse loop deve rodar:"))
soma = 0
for n in range(1,qtd + 1):
    print(f"Imprimindo {n}")
    num = int(input(f"Informe o {n}/{qtd} valor:"))
    soma += num
    pass
print(f"A soma é {soma}")

for indice,valor in enumerate(num):
    print(indice,valor)
    pass