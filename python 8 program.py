file=open("text.txt","r")
content=file.read()
max=0
max_occuring_word=""
occurances_dict={}
words=content.split()
for word in words:
    count=content.count(word)
    occurances_dict.update({word:count})
    if (count>max):
        max=count
        max_occuring_word=word
print("most occuring word is:",max_occuring_word)
print("no.of times it occured is:",max)
print("other word's frequency is:")
print(occurances_dict)
