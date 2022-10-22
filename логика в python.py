# Значение логического выражения: ((A и (не B))<=C)=A):

for a in range(2):
    for b in range(2):
        for c in range(2):
            F= (((a and (not b))<=c)==a)
            if F==False:
                print(f'a={a}, b={b}, c={c}')