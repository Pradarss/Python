stack=[]
top=0
while(top==0):
    print("STACK OPERATIONS")
    print("1. push")
    print("2. display stack")
    print("3. exit")
    ch=int(input("enter your choice="))
    if ch==1:
        bno=int(input("enter book no.="))
        bname=input("enter book name=")
        item=[bno,bname]
        stack.append(item)
        input()
    elif ch==2:
        display(stack)
        input()
    elif ch==3:
        break
    else:
        print("invalid choice!!!")
        input()

#page no.-6.23
#ques no.-7
