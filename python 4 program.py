import pickle
student_data={}
file=open("stud_data.dat","rb+")
try: 
   student_data=pickle.load(file)
   print(student_data)
except EOFError:   
      file.close()
