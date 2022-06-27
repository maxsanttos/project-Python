n = int(input("Informe um numero N:"))

e = 1
i = 1
for i in range(1,n+1):
    fat = 1
    for j in range(1,i+1): #While i <= n
        fat = fat * j
    e = e + 1/ fat

print(f"Resultado:{e}")



   
   