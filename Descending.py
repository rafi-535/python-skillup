import array as arr
n=int(input("Enter the legnth of the array:"))
a=arr.array('i',[])
for i in range(0,n):
    x=int(input("Enter an Element:"))
    a.append(x)
#print(a)
print("The original Array is:")
for e in a:

    print(e,end=' ')
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print('')
# Sorted in Descending order
print("Sorted list in Descending order:")
for i in range(0,len(a)):
    print(a[i],end=' ')