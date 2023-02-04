"a:12-249"
'-1'
'*7'
from itertools import product
for i in range(1,6):
    b= product('12', repeat=i)
    for n in b:
        prog=''.join(n)
        a=12
        for x in prog:
            if x=='1':
                a-=1
            elif x=='2':
                a*=7
            if a==489:print(prog)
