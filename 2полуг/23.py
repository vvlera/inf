"a:12-249"
'-1'
'*7'
from itertools import product
'''for i in range(1,6):
    b= product('12', repeat=i)
    for n in b:
        prog=''.join(n)
        a=12
        for x in prog:
            if x=='1':
                a-=1
            elif x=='2':
                a*=7
            if a==489:print(prog)'''
'''1-35
 1)+1
 2)*2'''
from itertools import product
def f(x,y):
    count=0
    for i in range(1,24):
        pr= list(product('12', repeat=i))
        if pr.count('2')>1:
            continue
        for g in pr:
            pr1=''.join(g)
            q=x
            for n in pr1:
                if n=='1': q+=1
                elif n=='2': q*=2
            if q>y or q==17: break  
            if q==y:
                count+=1
    return count
print(f(10,35)*f(1,10))

