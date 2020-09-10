t=int(input())

while(t>0):
    size=int(input())
    arr=[]
    for a in range(0,size):
        arr.append(list(map(int,input().split())))
    
    index=-1

    for val in range(0,size):
        if(val+1!=arr[0][val]):
            index=val+1

    check=[0]*index

    for val in range(1,index):
        if(val!=1 and arr[0][val]-arr[0][val-1]==1 ):
            check[val]=check[val-1]

        elif(val+1==arr[0][val]):
            check[val]=check[val-1]+1

        else:
            check[val]=check[val-1]
        
    a=set(check[1:])

    ans=0
    if(index!=-1):
        for val in a:
            if(val==0):
                ans+=1
            else:
                ans+=2
    print(ans)
    t-=1