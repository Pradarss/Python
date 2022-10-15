Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> File=open(“sample.txt”,”r”)
Data=file.read()
Print(data)
Vowels=0
Consonants=0
Upper=0
Lower=0
For ch in data:
      if str.isupper(ch):
           upper+=1
      elif str.islower(ch):
            lower+=1
      ch=str.lower(ch):
      if ch in “aeiou”:
Print(“no. of vowels:”, vowels)
Print(“no. of consonants:”,consonants)
Print(“no. of uppercase letters:”,upper)
Print(“no. of lowercase letters:”,lower)
