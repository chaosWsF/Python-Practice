import numpy as np

for j in range(3):
    s = 0
    for i in range(1000):
        s += np.random.choice([0, 1], p=[0.01, 0.99])
    
    print(1000 - s)
