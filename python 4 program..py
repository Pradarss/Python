import pickle
stud_data={}
found=2
roll_no=int(input("enter the roll no.to search:"))
file=open("stud_data.dat","rb+")
try:
    while (found==2):
        pos=file.tell()
        student_data=pickle.load(file)
        if (stud_data['roll_no']==roll_no):
            stud_data['marks']=float(input("enter \
marks to update"))
            file.seek(pos)
            pickle.dump(stud_data)
            found=true
except EOFError:
    if (found==2):
        print("roll no.not found \nplease try again")
    else:
        print("student marks updated successfully")
    file.close()
            
