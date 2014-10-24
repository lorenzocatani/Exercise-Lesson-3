from numpy import array, any, sum, exp, log

def energy(f,density):
  density = array(density)
  if density.dtype.kind != 'i' and len(density) > 0:
    raise TypeError ("Expected array of *integers*.")
  if any (density < 0):
    raise ValueError ("Expected array of *positive* integers.")
  E=0
  for element in density:
	   E = f(element) + E   
  return E

def ChangeParticle(density,i,direction):
  density = array(density)
  
  density[i] = density[i]-1 # Move a particle from the i-th position.
  d=len(density) 
  if i==d-1 and direction==1: density[0]=density[0]+1
  elif i==0 and direction==0: density[d-1]=density[d-1]+1
  elif direction==0 : density[i-1]= density[i-1]+1 # Particle moved on the left
  else : density[i+1]=density[i+1]+1 # Particle moved on the right
  return density