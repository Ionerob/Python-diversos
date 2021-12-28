ini = int(input())
final = int(input())
cont = 0
acum = int(0)
guarda =int(ini)
while ini < final:
    cont = cont + 1
    acum = ini * cont
print(f"O numero {guarda} tem {cont} multiplos menores que {final}")
