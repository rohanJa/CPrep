import math
t=int(input())

while(t>0):
    n,x=map(int,input().split())
    
    money=list(map(int,input().split()))
    l=-1
    for i in range(0,n):
        if(l<money[i]):
            l=money[i]
    
    r=int(math.ceil(l/x))
    rank=1
    turn={}

    for i in range(0,n):
        k=math.ceil(money[i]/x)
        if(k not in turn):
            turn[k]=[i+1]
        else:
            turn[k].append(i+1)
    ans=[]
    for i in sorted(turn.keys()):
        ans.extend(turn[i])
    print("Case #"+str(t)+":",end=' ')
    for val in range(0,n):
        print(ans[val],end=' ')
    print
    t-=1