a = 'ми'
alfa = ['и','м']
matr = [['***    ***','****  ****','*** ** ***'],['***   ***','*** * ***','****  ***']] #создание букв из звуздочек
ch =[alfa.index(z) for z in a] #список со порядковым значением буквы
for i in range(len(matr[0])): #перебор первого элемента списка matr для создания буквы из символов
    for g in range(len(ch)):
        print(matr[ch[g]][i],end =' ' ) # печать буквы
    print() # переход на следующую букву
    
    
for g in ch:
    print(matr[g][i],end =' ')
'''a1 = matr[0]
a2 = matr[1]
a3 = matr[2]

print(a,*a1,*a2,*a3,end ='\n')'''
    


'''
***    *** ***   ***
****  **** *** * ***
*** ** *** ****  *** '''   # - образец
