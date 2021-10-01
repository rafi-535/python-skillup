from array import *
x=array('i',[])
n=int(input("Enter The length Of an array:"))

for i in range(0,n):
    e=int(input("Enter The Elements of array:"))
    x.append(e)
print(x)
k=0
for i in range(0,len(x)):
   if(k<x[i]):
       k=x[i]
print(k)
