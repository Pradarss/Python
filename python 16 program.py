def check_primeALL(N):
    print("prime no.between 2 and N")
    for num in range(2,N+1):
        for i in range(2,num):
            if num%i==0:
                j=num/i
                break
            else:
                print(num,end="\t")
check_primeALL(20)

#page no.-3.29
#ques no.-38                
