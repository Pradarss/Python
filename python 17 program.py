choice='y'
total=0.0
while choice=='y' or choice=='Y':
    item_price=int(input("enter the item price="))
    gst=int(input("enter the gst on item="))
    total=total+(item_price+(item_price*gst)/100)
    choice=input("press y to continue\n\
else press n \n=>")
print("total amount to be paid=",total)

#page no.-1.24

