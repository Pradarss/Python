f=open("text.txt","r")
lines=f.readlines()
for line in lines:
    words=line.split(" ")
    for word in words:
        print(word+"# a",end="")
f.close()
