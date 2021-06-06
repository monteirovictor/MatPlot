import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[2,3,7,1,0]

titulo="Graph Bar"
eixox="Eixo X"
eixoy="Eixo y"


#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#rodar
plt.bar(x,y)
plt.show()