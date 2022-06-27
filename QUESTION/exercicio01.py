a = [1,0,5,-2,-5,7]
print(a)

#soma
soma = a[0] + a[1] + a[5]
print(soma)

#Alterando
a.pop(4)
print(a)

a.insert(4,100)
print(a)

#Mostrando a volar de cada linha

for indice,valor in enumerate(a):
    print(indice,"=",valor)
    pass