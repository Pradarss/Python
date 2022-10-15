#main
import rectangle
import circle
choice=0
ch='y'
while(ch=='y'):
    print("##MENU##")
    print("\n1. Area of circle")
    print("2. Circuference of a circle")
    print("3. Area of rectangle")
    print("4. Perimeter of rectangle")
    choice=int(input("\nEnter your choice=>"))
    if(choice==1):
        radius=int(input("Enter the \
circle's radius :"))
        print("The area is ",\
              circle.area(radius))
    elif(choice==2):
        radius=int(input("Enter the \
circle's radius :"))
        print("The circumference is ",\
              circle.circumference(radius))
    elif(choice==3):
        width=int(input("Enter the \
rectangle's width :"))
        length=int(input("Enter the \
rectangle's length :"))
        print("The area is ",\
              rectangle.area(width,length))
    elif(choice==4):
        width=int(input("Enter the \
rectangle's width :"))
        length=int(input("Enter the \
rectangle's length :"))
        print("The perimeter is ",\
              rectangle.perimeter(width,length))
    else:
        print("ERROR : Invalid selection")

#page no.-3.12
