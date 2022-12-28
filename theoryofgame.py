def f(a,b):
    if a==2:
        b=b*2
        c=10
        g=c-b
        return g
    elif a==1:
        b+=2
        c=10
        g=c-b
        return g
a=int(input('Какой из игроков победил?\n'))
b=int(input('За какое количество ходов человек выиграл?\n'))
if b<0 or b>10 or a>5 or a<0:
    print('Ошибка! Вводите значения в диапозоне от 0 до 10')
else:
    print(f'{f(a,b)} - количество камней в начале игры')

        
        
            
                
        
        
        
