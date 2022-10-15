def capitalise_sentence():
    f1=open("text.txt","r")
    f2=open("binary.txt","w")
    while 1:
        line=f1.readline()
        if not line:
            break
        line=line.rstrip()
        linelength=len(line)
        str=''
        str=str+line[0].upper()
        i=1
        while i<linelength:
            if line[i]==".":
                str=str+line[i]
                i=i+1
                if i>=linelength:
                    break
                str=str+line[i]
            else:
                str=str+line[i]
            i=i+1
            f2.write(str)
        else:
            print("source file does not exist")
    f1.close
    f2.close
capitalise_sentence()

#page no.-4.25
