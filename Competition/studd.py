t=int(input())

while(t>0):
    size=int(input())
    boys=list(map(int,input().split()))
    girls=list(map(int,input().split()))
    boys.sort()
    girls.sort()

    flag=1
    for i in range(0,size):
        if(boys[i]>girls[i]):
            flag=0
            break
        else:
            flag=1
            break
        
    if(flag==0):
        count=0
        for i in range(0,size):
            if(boys[i]>=girls[i]):
               count+=1
        if(count==size):
            print("YES")
        else:
            print("NO")
    else:
        count=0
        for i in range(0,size):
            if(boys[i]<=girls[i]):
               count+=1
        if(count==size):
            print("YES")
        else:
            print("NO")
    t-=1