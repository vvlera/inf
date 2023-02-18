with open('17.txt') as f:
    a=[int(x) for x in f]
    #print(a)
    count=0
    b=[]
    for x in a:
        if x%10==3: b.append(x)
    msq=max(b)**2
    #print(max(b))
    for i in range(len(a)-1):
        if abs(a[i])%10==3 and  abs(a[i+1])%10!=3 or abs(a[i])%10!=3 and abs(a[i+1])%10==3:
            if a[i]**2 + a[i+1]**2>msq:
                count+=1
print(count)
a=-10
print(abs(a%10))
            
