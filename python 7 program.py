stack=[]
max_capacity=3
print("Press 1 for pushing an element in \
stack.")
print("Press 2 for removing an element \
from stack.")
print("Press 3 for displaying all the elements \
of stack.")
while(max_capacity==3):
    
     choice=int(input("enter your choice:"))
     if choice==1:
        if(len(stack)==max_capacity):
            print("stack over flow...!!!!")
        else:
            val=int(input("enter no. to push:"))
            stack.append(val)
     elif(choice==2):
        if(len(stack)==0):
            print("stack underflow...!!!!")
        else:
            n=stack.pop()
            print(n,"removed from stack")
     elif(choice==3):
        top=stack[-1]
        print("all elements of stack are:")
        print(stack)
     else:
        break
