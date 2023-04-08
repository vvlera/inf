a = 'ми'
alfa = ['и','м']
matr = [['***    ***','****  ****','*** ** ***'],['***   ***','*** * ***','****  ***']]
ch =[alfa.index(z) for z in a]
for i in range(len(matr[0])):
    for g in range(len(ch)):
        print(matr[ch[g]][i],end =' ' )
    print()
'''a1 = matr[0]
a2 = matr[1]
a3 = matr[2]

print(a,*a1,*a2,*a3,end ='\n')'''
    


'''
***    *** ***   ***
****  **** *** * ***
*** ** *** ****  *** '''   
