def file_long(filename):
    filename=open("text.txt","r")
    longest=""
    for line in open("text.txt"):
        if len(line)>len(longest):
            longest=line
    print("longest line's length=",len(longest))
    print(longest)

file_long("text.txt")

