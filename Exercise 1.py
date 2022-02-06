import matplotlib.pyplot as plt
import numpy as np
from sys import exit

#General parabola function
def genparabola(x,a,b,c):
    result=a*x**2+b*x+c
    return result

#Parabola chosen with a minimum and two real roots
def parabola(x):
    result=genparabola(x,1,0,-4)
    return result

#Function that finds the mean of two numbers
def mean(a,b):
    result=0.5*(a+b)
    return result

#Input parameters
start=-5 #Starting x value
end=5 #Final x value
dx=0.1 #x incrememt
x1=-1 #Initial x1
x3=4 #Initial x3
tol=0.0001 #Root tolerance

#Calculating f(x) and graphing
i=start
graph=[]
while i<end-dx:
    graph.append(parabola(i))
    i=i+dx
x=np.linspace(start,end,len(graph))
plt.plot(x,graph)
plt.plot(x,0*x)
plt.xlim(min(x),max(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

#Check whether x1 and x2 are valid, telling which isn't, and aborting appropriately
if parabola(x1)>0 and parabola(x3)<0:
    print("x1 and x3 are invalid")
    exit(0)
if parabola(x1)>0 and not parabola(x3)<0:
    print("x1 is invalid")
    exit(0)
if not parabola(x1)>0 and parabola(x3)<0:
    print("x3 is invalid")
    exit(0)
 
#Calculating mean, resetting x1 and x2 appropriately
x2=mean(x1,x3)
if parabola(x2)>0:
    x3=x2
else:
    x1=x2
print("First new evaluations:")
print("x1:",x1)
print("x3:",x3)

#New plot showing (x2,f(x2))
plt.plot(x,graph)
plt.plot(x2,parabola(x2),'go')
plt.annotate("(x2, f(x2))",(x2+3*dx,parabola(x2)+3*dx))
plt.plot(x,0*x,'k')
plt.xlim(min(x),max(x))
plt.ylim(min(graph)-2,max(graph))
plt.plot(np.zeros(len(graph)),np.linspace(min(graph)-2,max(graph),len(graph)),'k')
plt.plot(-1,0,'ro')
plt.plot(4,0,'ro')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.annotate("x1",(-1-1.5*dx,5*dx))
plt.annotate("x3",(4-1.5*dx,5*dx))
plt.savefig("plotyoke.png",dpi=300)
plt.show()


#Function that returns root, given x1, x3, and tolerance
#root(x1,x3,tol)
def root(a,b,d):
    c=mean(a,b)

    while abs(parabola(c))>d:
        if parabola(c)>0:
            b=c
        else:
            a=c
        c=mean(a,b)
    return c

#Function that returns roots, with nsteps, given x1, x3, and tolerance
#(Returns as list, with 0th entry being root and 1st being nsteps)
def rootwithnsteps(a,b,d):
    nsteps=0
    c=mean(a,b)
    while abs(parabola(c))>d:
        if parabola(c)>0:
            b=c
        else:
            a=c
        #print("No no please help me")
        nsteps=nsteps+1
        c=mean(a,b)
    listt=[c,nsteps]
    return listt

#Graphing nsteps versus logarithm of tolerance
x1=-1.5
x3=3
logtollength=2500 #Number of points on graph
logtolgraph=np.linspace(-15,1,logtollength)
nstepsgraph=[]
for i in logtolgraph:
    nstepsgraph.append(rootwithnsteps(x1,x3,10**i)[1])
plt.plot(logtolgraph,nstepsgraph)
plt.xlabel("log(Tolerance)")
plt.ylabel("Number of Steps")
plt.ylim(0)
plt.savefig("plot1.png",dpi=300)
plt.show()