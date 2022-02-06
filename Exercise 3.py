import numpy as np
import math
import matplotlib.pyplot as plt

#Input parameters
start=0.02 #Initial x value
end=1.00 #Final x value
dx=0.0001 #x increment
A=1090 #Constant from equation
p=0.033 #Constant from equation
e2div4piep=1.44 #Constant from equation


#Interaction potential function
def function(x):
    value=A*np.exp(-(x/p))-e2div4piep/x
    return value

#First derivative of potential function
def deriv(x):
    value=e2div4piep/(x**2)-(A*np.exp(-(x/p)))/p
    return value

#Second derivative of potential function
def deriv2(x):
    value=A*np.exp(-(x/p))/(p**2)-(2*e2div4piep)/(x**3)
    return value

i=start
graph1=[]
graph2=[]
while i<end:
    graph1.append(function(i))
    graph2.append(-deriv(i))
    i=i+dx
x=np.linspace(start,end,len(graph1))
xgraph=np.linspace(0,end,len(graph1))
plt.plot(xgraph,0*xgraph,'k')
plt.plot(np.zeros(len(graph1)),np.linspace(-20,30,len(graph1)))
plt.plot(x,graph1)
plt.ylim(-20,30)
plt.xlabel("x")
plt.ylabel("V(x)")
plt.xlim(0,end)
plt.savefig("plotyokeyokeyoke.png",dpi=300)
plt.show()

plt.plot(xgraph,0*xgraph,'k')
plt.plot(np.zeros(len(graph1)),np.linspace(-20,30,len(graph1)))
plt.plot(x,graph2)
plt.ylim(-20,30)
plt.xlabel("x")
plt.ylabel("F(x)")
plt.xlim(0,end)
plt.savefig("plotyokeyokeyokeyoke.png",dpi=300)
plt.show()

def root(a,b):
    x1=a
    while abs(deriv(x1))>b:
        x1=x1-deriv(x1)/deriv2(x1)
    return x1


