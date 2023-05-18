with open('24-241.txt') as f:
        r = f.readline()
        r1 = r.split('E')
        mini = 999999999
        for i in r1:
            y = 0
            if i.count('B')>=2 and i.count('A')>5:
                y = i
                r3 = i.split('B')
                sp = []
                p = 0
                for x in r3:
                    if x.count('A')>5:
                        p = len(i)+2
                        mini = min(p,mini)
                    
print(mini)

        

                
            
        
# ответ - 13
