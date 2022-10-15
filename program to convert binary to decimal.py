s="United Nations"
for i in range(len(s)):
 if i%2==0:
   print(s[i],end= ' ')
 elif s[i]>='a' and s[i]<='z':
   print('*', end= ' ')
 elif s[i]>='A' and s[i] <='Z':
   print(s[i:],end= ' ')
