import numpy as np
a = np.array([[1,2,3,4], 
              [5,6,7,8]])

other = 1 - a
print(other)
print(np.concatenate([a, other], axis=0))