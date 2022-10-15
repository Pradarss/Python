queue=[]
top=0
while(top==0):
    print("QUEUE OPERATIOS")
    print("1. enqueue")
    print("2. dequeue")
    print("3. display queue")
    print("4. exit")
    ch=int(input("enter your choice="))
    if ch==1:
        print("for the new member, \
enter details below:")
        memberno=int(input("member no.="))
        membername=input("member name=")
        age=int(input("member's age="))
        item=[memberno,membername,age]
        queue.append(item)
        input("press enter to continue...")
    elif ch==2:
        item=queue.pop()
        if item=="underflow":
           print("underflow! \nqueue is empty",item)
        else:
            print("dequeue-ed item is",item)
        input("press enter to continue...")
    elif ch==3:
        print(queue)
        input("press enter to continue...")
    elif ch==4:
        break
    else:
        print("invalid choice!!!")
        input("press enter to continue...")

#page no.-6.24
#ques no.-8
