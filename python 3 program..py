import pickle
file=open("stud_data.dat","rb")
list_of_students=pickle.load(file)
r=int(input("enter roll no. to search:"))
for i in list_of_students:
    if (i['roll_no']==r):
        print(i['name'],"found in file")
if (i['roll_no']!=r):
    print("no student data found \
\nplease try again")
