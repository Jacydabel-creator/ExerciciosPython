altura1 = 0
altura2 = 0
altura3 = 0


for i in range(0, 10):
    altura = float(input('informe sua altura: '))

    if altura < 1.60:
        altura1 += 1
    if altura >= 1.60 and altura <= 1.80:
        altura2 += 1
    if altura > 1.80:
        altura3 += 1


print('quantidade de pessoas com altura menor que 1.60:', altura1)
print('quantidade de pessoas com altura entre 1.60 e 1.80:', altura2)
print('quantidade de pessoas com altura maior que 1.80:', altura3)
