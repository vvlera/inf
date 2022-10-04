p = int(input('Введите основание СС исходного числа: p = '))
valid = False
while valid == False:
    Np = (input(f'Введите исходное число: N{p} = '))
    for i in range(1, len(Np)):
        if int(Np[i]) >= p:
            print('Недопустимое число!')
            valid = False
            break
        else:
            valid = True
            Np = int(Np)
k = int(1)
N10 = int(0)
while not Np == 0:
    N10 = N10+(Np%10)*k
    k = k*p
    Np = Np//10
print(f'N10 = {N10}')
