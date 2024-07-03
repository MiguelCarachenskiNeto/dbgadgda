import os
from datetime import datetime

estacoes = ["Outono", "Inverno", "Primavera", "Verão"]

data = input('\nInsira uma data em formato dd/mm: ')
day, month = map(int, data.split('/'))
print("")
print(day, month)


if ((data > "20/03") (data =>)):
    valor = 0 
    print(estacoes[valor])
elif (data <"21/12"):
    valor = 1
    print(estacoes[valor]) 
elif (data < "22/09"):
    valor = 2
    print(estacoes[valor])
elif (data < "20/06"):
    valor = 3
    print(estacoes[valor])
else:
    print("erro")







