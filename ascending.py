from array import *
arr=array ('i',[])
n=int(input("Enter The Number Of Elements:"))
for i in range(n):
    x=int(input("Enter the Value:"))
    arr.append(x)
#print(arr)# print array as it is
print("Original Array")
for i in range(0,len(arr)):
    print(arr[i],end='  ')# Print only elements of array
#Sorting The Elements of Array
for k in range(0,len(arr)):
    for j in range(k+1,len(arr)):
        if(arr[k]>arr[j]):
            temp=arr[k]
            arr[k]=arr[j]
            arr[j]=temp
print('')
# Displaying the Elements of Array
print("Elements sorted in ascending Order ")
for i in range(0,len(arr)):
    print(arr[i],end='  ')

