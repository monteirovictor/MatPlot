import matplotlib.pyplot as plt
import random

vetor=[]

for i in range(100):
    num_aletorio=random.randint(0,50)
    vetor.append(num_aletorio)
    
plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()