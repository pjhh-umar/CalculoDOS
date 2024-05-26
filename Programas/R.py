import matplotlib.pyplot as plt
import numpy as np
import os

a = 0; b = 100 #Aquí se define el intervalo
k=10000  #Número de puntos a gráficar
# Enseguida se define la función f(x) mediante su regla de correspondencia:
def f(x):
    fun = 'x**2'
    return eval(fun)

z = np.linspace(a,b,k) #Array con los puntos que se van a utilizar para gráficar
y = f(z) #Arrar con las imagenes de los puntos en z

n=int(input("¿CUANTOS RECTANGULOS DESEAS DIBUJAR?")) #Número de puntos en la particion del intervalo [a,b]

plt.figure(figsize=(6.5,6.5))
#Se "dibujan" los ejes
plt.axhline(0, linestyle='-', linewidth=1, color='black')
plt.axvline(0, linestyle='-', linewidth=1, color='black')
#Se dibuja la grafica de la función f(x)  y se sombrea el area debajo de la gráfica
# plt.fill_between(z,y,color='cyan', alpha=1)#Inscritos
#plt.fill_between(z,y,color='gray', alpha=0.5)#Circunscritos
plt.fill_between(z,y,color='cyan', alpha=1)
plt.plot(z,y, color = 'red', linewidth = 1.5)


    
    
x = np.linspace(a,b,n)  #Array que determina la partición homegenea de [a,b] de longitud n
delta = (b-a)/n #Longitud de cada uno de los subintervalos determinados por dos puntos consecutivos de la partición homogenea
for i  in range(len(x)-1):
    #Graficamos los rectangulos inscritos
    mi = f(x[i])
    plt.plot([x[i],x[i+1]], [mi,mi], color = 'darkblue', linewidth = 1)
    plt.fill_between([x[i],x[i+1]], [mi,mi], color='darkblue', alpha=0.2)
    plt.vlines([x[i],x[i+1]], ymin = min(0,mi), ymax= max(0,mi), linestyle = '--',color = 'w', linewidth =1.5 )
    # Graficamos los rectangulos circunscritos    
    Mi = f(x[i+1])
    plt.plot([x[i],x[i+1]], [Mi,Mi], color = 'green', linewidth = 1)
    plt.fill_between([x[i],x[i+1]], [Mi,Mi], color='green', alpha=0.15)
    plt.vlines([x[i],x[i+1]], ymin = min(0,Mi), ymax= max(0,Mi), linestyle = '--',color = 'w', linewidth =1.5 )


xi=[]
for i in range(0,n):
    xi.append("x" +str(i))
    if i==n-1:
        xi[n-1]=xi[n-1]+"=b"
    elif i==0:
        xi[0]=xi[0]+"=0"
if n<=12:
    plt.xticks(x,xi)    
else:
     plt.xticks([a,b],["x0=0","x"+str(n)+"=b"])    
plt.yticks([]) 
# plt.title('')
plt.show()