with open('26.txt') as f:
    ls = [int(x) for x in f]
    ls = sorted(ls[1:], reverse=True)
    c, mini = 1, ls[0]
    for i in range(1, len(ls)):
        if ls[i]+3 <= mini:
            mini = ls[i]
            c+=1
print(c,mini)
