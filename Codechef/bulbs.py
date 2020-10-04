t=int(input())

while(t>0):
    s=str(input())
    side=[]
    count=0
    i,j=0,len(s)
    if(s[0]=='0'):
        for val in s:
            if(val=='0'):
                count+=1
            else:
                side.append(count)
                i=count+1
                count=0
                break
    if(s[len(s)-1]=='0'):
        for val in s[-1::-1]:
            if(val=='0'):
                count+=1
            else:
                j=len(s)-count
                side.append(count)
                break
    print(side)
    mid=[]
    count=0
    for val in range(i,j):
        if(s[val]=='0'):
            count+=1
        elif(count!=0):
            mid.append(count)
            count=0
    mid.sort(reverse=True)
    side.sort(reverse=True)


    # while(k>0):
    #     if()


    print(mid)

    t-=1