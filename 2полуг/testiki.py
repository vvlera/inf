'''cout = 0
h=0
for x in range(10,1000001):
    cout=0
    li= str(x)
    for y in li:
        cout += int(y)**len(li)
    if cout==x:
        h+=x
#print(h)  #810010'''


cut=[]
for i in range(540,570):
    s=str(i)
    maxi = max(s) + max(x for x in s if x!=max(s))
    mini = min(s) + min(y for y in s if y!=min(s))
    if int(max)-int(min)==10:
        cut.append(i)
        a= sum(cut)
print(a)
        


    
