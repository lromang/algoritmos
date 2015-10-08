import numpy as np

##Get the length of an integer
def int_length(integer):
  return np.floor(np.log(integer,10)) + 1
