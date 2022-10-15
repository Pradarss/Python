def max_of_two(x,y):
    if x>y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))
x=int(input("enter first no.-"))
y=int(input("enter second no.-"))
z=int(input("enter third no.-"))
print(max_of_three(x,y,z))

#page no.-2.51
#ques no.-16
