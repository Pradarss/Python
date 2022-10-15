import pickle
file=open("stud_data.txt","rb")
r=int(input("enter the rollno to search"))
found=0
try:
    while True:
        data=pickle.load(file)
        if data["roll"]==r:
              print("record found")
              print(data)
              found=1
except EOFError:
    pass
if found==0:
    print("record not found")
file.close()
