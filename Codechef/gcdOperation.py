t=int(input())
while(t>0):
    n=int(input())
    l=list(map(int,input().split()))
    temp=[i+1 for i in range(0,n)]
    
    flag=1    
    for val in range(0,n):
        if(temp[val]%l[val]==0 and l[val] in temp):
            pass
        else:
            flag=0
            break
    if(flag):
        print("YES")
    else:
        print("NO")

    t-=1