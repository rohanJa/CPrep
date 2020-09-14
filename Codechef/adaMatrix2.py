t=int(input())

while(t>0):
    size=int(input())
    arr=[]
    for a in range(0,size):
        arr.append(list(map(int,input().split())))

    ans=0
    transposed=False
    for i in range(size-1,0,-1):
        need_to_transposed = (arr[i][0]==i+1)   #if element is equal to the coloumn
        # if it is transposed earlier then we didnot need to transfer
        if(need_to_transposed ^ transposed):  #checks the status of the transpose
            ans+=1
            transposed=not transposed

    print(ans)
    t-=1