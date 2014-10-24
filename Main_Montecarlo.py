from Montecarlo import energy,ChangeParticle,CompareEnergies 
from numpy import array, any, sum, exp, log
import random

density0=[12,23,14,24,16,23,32]
d = len(density0)
T=273.5


def f(density): 
 density=array(density)
 return 0.5 * sum(density * (density-1))

j= range(100) 

for value in j:
 i = random.randint(0,d-1)
 direction=random.randint(0,1)
 p1=random.random()
 E0=energy(f,density0)
 density1=ChangeParticle(density0,i,direction)
 E1=energy(f,density1)
 a=CompareEnergies(E0,E1,T,p1)
 if a==1:
  density0=density1
  print density0