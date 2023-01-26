#12
a=[]
for i in range(2,1000):
    if all(i%x!=0 for x in range(2,i)):
        a.append(i)
        for n in range(2,1000):
            sum=117+4*n
            if sum==i:
                print(n)
                
#14
#123x5(15)+1x233(15)
a='0123456789abcde'
for x in a:
    f=int(f'123{x}5',15)+ int(f'1{x}233',15)
    if f%14==0:
        print(x,f//14)
#15
#((x%2==0)<=(x%3!=0))  or (x+A>=100)
for a in range(1,100):
    if all(((x%2==0)<=(x%3!=0))  or (x+a>=100) for x in range(1,1000)):
        print(a)
        break
