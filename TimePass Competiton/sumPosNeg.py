t=int(input())

while(t>0):
    sum1=0
    sum2=0
    n=int(input())
    l=set(map(int,input().split())) 

    for i in l:
        if(i>0):
            sum1+=i
        else:
            sum2+=i
    
    print(str(sum1)+" "+str(sum2))
    t-=1