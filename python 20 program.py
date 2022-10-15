from random import randint


def fill_list(I,limit_num,low,high):
    for i in range(limit_num):
        I.append(randint(low,high))

minimum=int(input("Min :"))
maximum=int(input("Max :"))
n=int(input("Numbers limit :"))
a=[]
fill_list(a,n,minimum,maximum)
print(a)


#page no.-2.18
