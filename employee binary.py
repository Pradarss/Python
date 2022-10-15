import pickle
employee_data={}
list_of_employees=[]
no_of_employees=int(input("enter no. of employees:"))
for i in range(no_of_employees):
    employee_data["empno"]=int(input("employee no.:"))
    employee_data["ename"]=input("employee name:")
    employee_data["salary"]=int(input("salary:"))
    list_of_employees.append(employee_data)
    stud_data={}
file=open("employee_data.dat","wb")
pickle.dump(list_of_employees,file)
file.close()
