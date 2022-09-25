import random
import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
from numpy import trapz


#1.3

#x=5>=2
#A={1,3,7,8}
#B={2,4,5,10}
#C=A&B
#df='Антонова Антонина',34,'ж'
#z='type'
#D=[1,'title',2,'content']
#print(x," ",type(x))
#print(A," ",type(A))
#print(B," ",type(B))
#print(C," ",type(C))
#print(df," ",type(df))
#print(z," ",type(z))
#print(D," ",type(D))

                                                                 #2.3
#x=int(input())
#if x>5:
#    print("x (5;+infinity) ")
#elif x>-5:
 #   print("x [-5;5]")
#else:
 #   print("x (-infinity,-5)")

                                                                #3.3.1

#x=int(10)
#while x > 0:
 #   print (x)
 #   x-=3

                                                                #3.3.2
#s=list(["рост","вес","возраст","пол"])

#for person in s:
#    print(person)

                                                                 #3.3.3
#i=2
#s=list()
#while i<=15:
#    s.append(i)
#    i+=1
#print(s)  

                                                                #3.3.4
#for i in range(105,4,-25):
 #   print(i)

                                                                 #3.3.5
#x=[0,1,2,3,4,5,6,7,8,9]
#i=len(x)-1

#while i>len(x)/2:
#    if(i%2==0):
#       z= x[i]
#       x[i]=x[len(x)-i-2]
#       x[len(x)-i-2]=z
      

#    i-=1;
#print(x)

                                                            #4.3.1
#x=[0,1,2,3,4,5,6,7,8,9]
#y=[0,1,2,3,4,5,6,7,8,9]
#s=0.0

#i=0;
#while i<10:
  #  x[i]=random.random()
 #   s+=x[i]
 #   #y[i]=random.random()
   # i+=1
#plt.scatter(y,x,marker=".",c="r")
#print(s/10)
                                                        
                                                                #4.3.2

#x=np.arange(1,11,1)
#y=np.log(2*x)+(np.sqrt(1+np.cos(np.power(x, 2))+np.exp(np.sqrt(x))))/(1-np.sin(np.power(x, 3)))
#x1=np.arange(1,6,1)
#plt.grid()
#plt.plot(x,y,c="b")
#plt.show()
#y=np.abs(np.log(2*x1)+(np.sqrt(1+np.cos(np.power(x1, 2))+np.exp(np.sqrt(x1))))/(1-np.sin(np.power(x1, 3))))
#plt.scatter(x1, y,marker=".",c="r")
#plt.show()
                                                                
                                                                    #4.3.3
#x=np.arange(1,10,1)
#y=np.abs(np.abs(np.cos(x*np.exp(np.cos(x)+np.log(x+1)))))

#plt.plot(x,y,c="g")
#plt.fill_between(x, y)
#print("S=",trapz(y))
                        
                                                        #4.3.4
#fig = plt.figure()
#fig2 = plt.figure()
#fig3 = plt.figure()
#month = ["Jan", "Feb", "Mar", "Apr", "May","June","July", "Aug", "Sept", "Oct","Nov","Dec"]
#priceAAPL = [131,121,122,131,124,136,145,151,141,149,165,177]
#priceGOGL = [91,101,103,117,117,122,134,144,133,148,141,144]
#priceMSFT = [231,232,235,252,249,270,284,301,281,331,330,336]
#print(type(fig))
#plt.plot(month, priceAAPL)
#print(type(fig2))
#print(fig2.axes)
#plt.plot(month, priceGOGL)
#print(type(fig3))
#print(fig3.axes)
#plt.plot(month, priceMSFT)
#plt.show()

                                                #4.3.5
print("Введите x,y и операцию")
x="a"
isnegative=False
y="a"
while(not(x.isdigit())):
    x=input()
    if(x[0]=='-'):
        x=x.replace('-','')
        isnegative=True
    else:
        isnegative=False
x=float(x)
if (isnegative):
    x*=-1
while(not(y.isdigit())):
    y=input()
    if(y[0]=='-'):
        y=y.replace('-','')
        isnegative=True
    else:
        isnegative=False
y=float(y)
if (isnegative):
    y*=-1
s=input()
while((s!="sin")and(s!="cos")and(s!="e")and(s!="^")and(s!="+")and(s!="-")and(s!="*")):
    s=input()
if(s=="sin"):
    print("sin(x+y)=",np.sin(x+y))
elif (s=="cos"):
    print("cos(x+y)=",np.cos(x+y))       
elif(s=="+"):
    print("x",s,"y=",x+y)
elif(s=="-"):
    print("x",s,"y=",x-y)
elif(s=="*"):
    print("x",s,"y=",x*y)
elif(s=="/"):
    print("x",s,"y=",x/y)
elif(s=="e"):
    print("e^(x+y)=",np.exp(x+y))
else:
    print("x^y=",np.power(x, y))