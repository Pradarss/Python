def Lshift(arr,n):
    L=len(arr)
    for x in range(0,n):
        y=arr[0]
        for i in range(0,L-1):
            arr[i]=arr[i+1]
        arr[L-1]=y
    print(arr)

Lshift([10,20,30,40,12,11],2)
