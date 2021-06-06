from matplotlib import colors
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,3,7,1,0]

titulo="Graph Scatterplot"
eixox="Eixo X"
eixoy="Eixo y"


#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#rodar
plt.scatter(x,y,label="meus pontos",color="k",marker="^",s=100)
plt.legend()
plt.plot(x,y,color="k",linestyle="--")

plt.show()

#save figuras
#plt.savefig("figura1.png")