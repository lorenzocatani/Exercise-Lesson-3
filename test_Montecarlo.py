from MonteCarloExercise import energy,ChangeParticle,CompareEnergies
from nose.tools import assert_equal
from mock import Mock
from numpy import array, any, sum, exp, log

def test_energy_not_integer():
  """ Test for integer numbers"""
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  try:  energy(f,['i',2,1])
  except: pass
  else: raise AssertionError("non integers did not raise an error")
  
def test_energy_not_positive():
  """ Test for positive numbers """
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  try:  energy(f,[-5,2,1])
  except: pass
  else: raise AssertionError("negative number did not raise an error")
  
def test_energy_right():
  """ The right one """
  # Test something
  # def f(x): return 0.5*x*(x-1)
  f = Mock(name="myroutine", return_value=2) 
  v=[3,2,1]
  expected=6
  actual=energy(f,v)
  assert_equal(expected,actual)