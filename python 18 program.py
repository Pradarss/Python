scl=dict()
i=1
flag=0
n=int(input("enter the no.of entries=>"))
while i<=n:
    adm=input("\nEnter admission no. of a student :")
    nm=input("Enter name of the student :")
    sec=input("Enter class and section of student :")
    per=float(input("Enter percentage of student :"))
    b=(nm,sec,per)
    scl[adm]=b
    i=i+1
I=scl.keys()

for i in I:
    print("\nAdmno=>",i)
    z=scl[i]
    print("name\t","class\t","per\t")
    for j in z:
        print(j,end="\t")


#page no.-1.40
