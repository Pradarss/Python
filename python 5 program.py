file=open("text.txt","r")
lines=file.readlines()
file.close()
file=open("text.txt","w")
file1=open("p.py","w")
for line in lines:
    if 'a' in line or 'A' in line:
        file1.write(line)
    else:
        file.write(line)
print("all line that contains character \
'a' has been removed")
print("p.py file",file1)
file.close()
file1.close()
