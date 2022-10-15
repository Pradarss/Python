result=0
val1=float(input("enter value 1:"))
val2=float(input("enter value 2:"))
op=input("enter any of the operator (+,-,*,/):")
while result==0:
    if op=="+":
        result=val1+val2
    elif op=="-":
        if val1>val2:
            result=val1-val2
        else:
            result=val2-val1
    elif op=="*":
        result=val1*val2
    elif op=="/":
        if val2==0:
            print("please enter a value other thsn 0")
        else:
            result=val1/val2
    else:
        print("please enter a valid operator")
    print("the result is : ",result)
