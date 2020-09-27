import math
t=int(input())
c=0
while(t>0):
    n,k=map(int,input().split())
    
    interval=[]
    for i in range(0,n):
        interval.append(list(map(int,input().split())))
    interval=sorted(interval)

    roboCount=0
    final=0

    for i in range(0,n):
        a=interval[i][0]
        if(final>interval[i][0]):
            a=final

        time=math.ceil((interval[i][1]-a)/k)
        final=a+k
        roboCount+=time
    c+=1
    print("Case #"+str(c)+": "+str(roboCount))
    t-=1