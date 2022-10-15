import pickle
stud_data={}
list_of_students=[]
no_of_students=int(input("enter no. of students:"))
for i in range(no_of_students):
    stud_data["roll_no"]=int(input("enter roll no:"))
    stud_data["name"]=input("enter name:")
    list_of_students.append(stud_data)
    stud_data={}
file=open("stud_data.dat","wb")
pickle.dump(list_of_students,file)
file.close()
