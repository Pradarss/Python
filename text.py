file=open("text.txt","w")
file.write("me:hello my name is adarsh \
\nishu:my name is ishu \
\nme:how are you \
\nishu:i am fine and you \
\nme:i am also fine \
\nishu:bye \
\nme:bye")
file.write("\nishu")
file.write("\nadarsh")
file.close
file=open("text.txt","r")
f=file.read
print(f)
