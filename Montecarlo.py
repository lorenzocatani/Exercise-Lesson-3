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