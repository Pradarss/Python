vowels=['a','e','i','o','u','A','E','I','O','U']
word=input("enter the word to search for vovels:")
stack=[]
for letter in word:
    if letter in vowels:
        if letter not in stack:
            stack.append(letter)
print(stack)
print("the no.of different vowels present in",word,"is",len(stack))

#page no.-6.7

