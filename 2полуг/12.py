sp=[]
for num in range(2,1000):
    n=0
    for delitel in range(2,100):
        if num%delitel==0: n+=1
    if n==0: sp.append(num)
print(sp)
    
flag=False
for i in sp:
    for y in range (100):
        if y*4+120==i and flag==False:
            print(y, i)
            flag=True
