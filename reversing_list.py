# two pointers method
array=[0,1,2,3,4,5]
first=0
last=len(array)-1
temp=0
while first<last:
    temp=array[first]
    array[first]=array[last]
    array[last]=temp
    last=last-1
    first=first+1
print(array)
