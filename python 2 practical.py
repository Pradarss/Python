f=open("text.txt","r")
data=f.read()
print(data)
vowels=0
consonants=0
upper=0
lower=0
for ch in data:
    if ch.isupper:
        upper+=1
    if ch.islower:
        lower+=1
    if ch.isalpha:
        if ch in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1
print("no. of vowels=",vowels)
print("no. of consonants=",consonants)
print("no. of upper case=",upper)
print("no. of lower case=",lower)
f.close()
