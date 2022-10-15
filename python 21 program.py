from random import randint

def bin_search(Ist,item):
    mid=len(Ist)//2
    low=0
    high=len(Ist)-1
    while Ist[mid]!=item and low<=high:
        if item>Ist[mid]:
            low=mid+1
        else:
            high=mid-1
    if low>high:
        return None
    else:
        return mid

a=[]
for i in range(10):
    a.append(randint(1,20))
a.sort()
print(a)

value=int(input("Enter element to search=> "))
print("Element found at the index : ",\
      bin_search(a,value))

#page no.-2.19
