import random
from matplotlib import pyplot as plt 


numero_a = range(1, 13)
numero_b = [random.randint(1, 1000) for i in range(12)]
plt.plot(numero_a , numero_b)
plt.show()