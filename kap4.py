while True: 
    n = int(input('?, Skriv ett tal <=0 för att sluta'))
    if n <= 0:
        break
    summa = 0
    k = 1
    while k <= n:
        summa = summa + k 
        k = k + 1
print('Summan blir', Summa)