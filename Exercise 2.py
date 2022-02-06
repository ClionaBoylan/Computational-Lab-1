import numpy as np
from decimal import *
import matplotlib.pyplot as plt

#General parabola function
def genparabola(x,a,b,c):
    result=a*x**2+b*x+c
    return result

#Parabola chosen with a minimum and two real roots
def parabola(x):
    result=genparabola(x,1,0,-4)
    return result

#Derivative of general parabola function
def genderiv(x,a,b):
    result=2*a*x+b
    return result

#Derivative of chosen parabola function
def deriv(x):
    result=genderiv(x,1,0)
    return result

#Input parameters
start=-5 #Starting x value
end=5 #Final x value
dx=0.1 #x increment

#Plotting f(x) and its derivative
i=start
graph1=[]
graph2=[]
while i<end-dx:
    graph1.append(parabola(i))
    graph2.append(deriv(i))
    i=i+dx
x=np.linspace(start,end,len(graph1))
plt.plot(x,graph1,label="f(x)")
plt.plot(x,graph2,label="f'(x)")
plt.legend()
plt.plot(x,0*x,'k')
plt.xlim(min(x),max(x))
plt.ylim(min(graph1)-2,max(graph1))
plt.plot(np.zeros(len(graph1)),np.linspace(min(graph1)-2,max(graph1),len(graph1)),'k')
plt.xlabel("x")
plt.savefig("plotyokeyoke.png",dpi=300)
plt.show()

x1=1 #Initialising x1
x1=x1-parabola(x1)/deriv(x1)
#Creating plot showing (x2,f(x2))
plt.plot(x,graph1)
plt.plot(x1,parabola(x1),'ro')
plt.annotate('(x1,f(x1))',(x1+3*dx,parabola(x1)+3*dx))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#Specifies number of decimal places to keep nsteps calculations (default is 16 or 17)
noplaces=1000
getcontext().prec=noplaces

tol=0.000001
def root(a,b):
    x1=a
    while abs(parabola(x1))>b:
        x1=x1-parabola(x1)/deriv(x1)
    return x1

def rootwithnsteps(a,b):
    x1=Decimal(a)
    nsteps=0
    while Decimal(abs(parabola(x1)))>Decimal(b):
        x1=x1-Decimal(parabola(x1))/Decimal(deriv(x1))
        nsteps=nsteps+1
    
    listt=[x1,nsteps]
    return listt

x1=root(1,tol)
    
print("x1:",x1)
print("f(x1):",parabola(x1))

x1=root(-3,tol)
    
print("x1:",x1)
print("f(x1):",parabola(x1))

test=10
logtollength=2500
logtolgraph1=np.linspace(-15,1,logtollength)
nstepsgraph1=[]
for i in logtolgraph1:
    nstepsgraph1.append(rootwithnsteps(test,10.00**i)[1])

plt.plot(logtolgraph1,nstepsgraph1)
plt.xlabel("Log(tolerance)")
plt.ylabel("Number of Steps")
plt.ylim(0)
plt.savefig("plot4.png",dpi=300)
plt.show()

def rootwithnstepsandmax(a,b,c):
    x1=a
    nsteps=0
    while Decimal(abs(parabola(x1)))>Decimal(b):
        x1=x1-Decimal(parabola(x1))/Decimal(deriv(x1))
        nsteps=nsteps+1
        if nsteps>c:
            print("Max steps reached")
            break
    
    listt=[x1,nsteps]
    return listt

