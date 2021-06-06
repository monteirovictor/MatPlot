import matplotlib.pyplot as plt
dados = open("populacao_brasileira.csv").readlines()

#ano
x=[]
#populacao
y=[]

for i in range(len(dados)):
    if i !=0:
        linha=dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.show()