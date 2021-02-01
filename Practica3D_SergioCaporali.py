"""
Generar un programa en Python que genere la grafica
Rotación 3D
autor; Sergio Caporali Ramirez
Fecha: 11/12/20

"""

import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, radians 

plt. axis([0,70,50,0],)
plt.axis('on')
plt.grid(True)

#___Lista de coordenadas
#    0   1  2  3   4   5  6  7
x=[-10,-10,10,10,-10,-10,10,10]#Coordenadas no rotadas
y=[-10,-10,-10,-10,10,10,10,10]
z=[-3,3,3,-3,-3,3,3,-3]

xg=[0,1,2,3,4,5,6,7]#Coordenadas globales
yg=[0,1,2,3,4,5,6,7]
zg=[0,1,2,3,4,5,6,7]

#____Definir las funciones

def rotRx(xc,yc,zc,xp,yp,zp,Rx):
    a=[xp,yp,zp]
    b=[1,0,.5]#---Rx11,Rx12,Rx13
    xpp=np.inner(a,b)#---Producto escalar de a,b=xp*Rx11+yp*Rx12+zp*Rx13
    b=[0,cos(Rx),-sin(Rx)]#---Rx21,Rx22,Rx23
    ypp=np.inner(a,b)#---Producto escalar de a,b=xp*Rx21+yp*Rx22+zp*Rx23
    b=[0,sin(Rx),cos(Rx)]#---Rx31,Rx32,Rx33
    zpp=np.inner(a,b)#---Producto escalar de a,b=xp*Rx31+yp*Rx32+zp*Rx33
    [xg,yg,zp]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]

def rotRy(xc,yc,zc,xp,yp,zp,Ry):
    a=[xp,yp,zp]
    b=[cos(Ry),0,sin(Ry)] #---Ry11,Ry12,Ry13
    xpp=np.inner(a,b)#---Producto escalar de a,b=xp*Ry11+yp*Ry12+zp*Ry13
    b=[0,1,0] #---Ry21,Ry22,Ry23
    ypp=np.inner(a,b) #---Producto escalar de a,b=xp*Ry21+yp*Ry22+zp*Ry23
    b=[-sin(Ry),0,cos(Ry)] #---Ry31,Ry32,Ry33
    zpp=np.inner(a,b)#---Producto escalar de a,b=xp*Ry31+yp*Ry32+zp*Ry33
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]

def rotRz(xc,yc,zc,xp,yp,zp,Rz):
    a=[xp,yp,zp]
    b=[cos(Rz),-sin(Rz),0] #---Rz11,Rz12,Rz13
    xpp=np.inner(a,b)#---Producto escalar de a,b=xp*Rz11+yp*Rz12+zp*Rz13
    b=[sin(Rz),cos(Rz),0] #---Rz21,Rz22,Rz23
    ypp=np.inner(a,b)#---Producto escalar de a,b=xp*Rz21+yp*Rz22+zp*Rz23
    b=[0,0,1] #---Rz31,Rz32,Rz33
    zpp=np.inner(a,b)#---Producto escalar de a,b=xp*Rz31+yp*Rz32+zp*Rz33
    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]
    return[xg,yg,zg]

def plotbox(xg,yg,zg):#--- trazar la caja usando las coordenadas de rotación xg,yg,zg
    for i in (0,1,2):#---trazar parte superior
        plt.plot([xg[i],xg[i+1]],[yg[i],yg[i+1]],linewidth=1,color='k')

        plt.plot([xg[3],xg[0]],[yg[3],yg[0]],linewidth=1,color='k') #---Cerrar parte superior

        for i in (4,5,6):#---trazar parte inferior
            plt.plot([xg[i],xg[i+1]],[yg[i],yg[i+1]],linewidth=1,color='k')

        plt.plot([xg[7],xg[4]],[yg[7],yg[4]],linewidth=1,color='k')#---cerrar la parte inferior
    
        for i in (0,1,2,3):#---trazar lados 
            plt.plot([xg[i],xg[i-4]],[yg[i],yg[i-4]],linewidth=1,color='k')

        plt.scatter(xc,yc,s=5)#---trazar el punto en el centro

def plotboxx(xc,yc,zc,Rx):
    for i in (0,1,2,3,4,5,6,7): #---rotar ocho esquinas
        [xg[i],yg[i],zg[i]]=rotRx(xc,yc,zc,x[i],y[i],z[i],Rx)
        
    plotbox(xg,yg,zg)

def plotboxy(xc,yc,zc,Ry):
    for i in (0,1,2,3,4,5,6,7):#---rotar ocho esquinas
        [xg[i],yg[i],zg[i]]=rotRy(xc,yc,zc,x[i],y[i],z[i],Ry)
          
    plotbox(xg,yg,zg)

def plotboxz(xc,yc,zc,Rz):
    for i in (0,1,2,3,4,5,6,7): #---rotar ocho esquinas
        [xg[i],yg[i],zg[i]]=rotRz(xc,yc,zc,x[i],y[i],z[i],Rz)

    plotbox(xg,yg,zg)
        
#---R=0 caja (a)

Rx=radians(10)
xc=35#---caja (a) coordenadas del centro
yc=35
zc=0
plotboxx(xc,yc,zc,Rx) #---usamos desde Rx=0 plotboxy o plotboxz

#___Listas de coordenadas

plt.text(30,7,'0',color='b')
plt.text(34,7,'1',color='b')
plt.text(38,7,'2',color='b')
plt.text(41,7,'3',color='b')
plt.text(45,7,'4',color='b')
plt.text(49,7,'5',color='b')
plt.text(53,7,'6',color='b')
plt.text(57,7,'7',color='b')

plt.text(25,10,'x=[-10,-10, 10, 10,-10,-10, 10, 10]')
plt.text(25,13,'y=[-10,-10,-10,-10, 10, 10, 10, 10]')
plt.text(25,16,'z=[  -3,   3,   3,  -3,  -3,   3,   3,  -3]')

#___Etiquetas

plt.text(8,7,'x=20')
plt.text(8,9.5,'y=20')
plt.text(8,11.9,'z=3')

#___Triangulo 1
x=np.array([5.2 , 6 , 6.8 , 5.2])
y=np.array([7 , 5.5 , 7 , 7])
plt.plot(x,y,color ='k',linewidth=1)
plt.plot(x,y,color ='k',linewidth=1)
#___Triangulo 2
x=np.array([5.2 , 6 , 6.8 , 5.2])
y=np.array([10 , 8.5 , 10 , 10])
plt.plot(x,y,color ='k',linewidth=1)
plt.plot(x,y,color ='k',linewidth=1)
#___Triangulo 3
x=np.array([5.2 , 6 , 6.8 , 5.2])
y=np.array([12 , 10.5 , 12 , 12])
plt.plot(x,y,color ='k',linewidth=1)
plt.plot(x,y,color ='k',linewidth=1)

plt.text(5.5,20,'xc=35')
plt.text(5.5,22,'yc=35')
plt.text(5.5,24,'zc=0')

plt.text(20,27,'0',color='b')
plt.text(26,24,'1',color='b')
plt.text(49,24,'2',color='b')
plt.text(41,28,'3',color='b')
plt.text(20,45,'4',color='b')
plt.text(29,43,'5',color='b')
plt.text(49,42,'6',color='b')
plt.text(41,48,'7',color='b')

plt.title('X')
plt.ylabel('Y')

plt.show()