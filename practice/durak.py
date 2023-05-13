cds = ['6c','7c','8c','9c','10c','Vc','Dc','Kc','Tc','6b','7b','8b','9b','10b','Vb','Db','Kb','Tb','6k','7k','8k','9k','10k','Vk','Dk','Kk','Tk','6p','7p','8p','9p','10p','Vp','Dp','Kp','Tp']
# k- крести, p- пики, c- черви, b- буби, cards - колода
print(len(cds))
masti = ['черви','буби','крести','пики'] #масти
from random import*
     
def game(cds):
     kozr = 0
     pl1 = []
     pl2 = []
     shuffle(cds) #тасовка карт
     kozr = choice(masti)
     for i in range(0,7):
          for g in cds:
               pl1= choice(cds)
               cds.remove(g)
     for x in range(0,7):
          for p in cds:
               pl2 = choice(cds)
               cds.remove(p)
     print(cds, len(cds), pl1, pl2)

game(cds)

        
          
