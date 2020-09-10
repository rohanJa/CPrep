t=int(input())

while(t>0):
    size=int(input())
    speed=list(map(int,input().split()))
    
    resultMax=1
    ansMax=1
    resultMin=99

    for val in range(0,len(speed)):
        resultMax=1
        minSpeed=speed[val]
        fastSpeed=speed[val]

        for j in range(0,len(speed)):
            if(j!=val):
                if(val>j and speed[j]>speed[val]):
                    resultMax+=1
                    if fastSpeed==speed[val]:
                        fastSpeed=speed[j]
                    else:     
                        fastSpeed=max(fastSpeed,speed[j])

                elif(val<j and speed[j]<fastSpeed):
                    resultMax+=1
            
        ansMax=max(ansMax,resultMax)
        resultMin=min(resultMax,resultMin)
            

    print(str(resultMin)+" "+str(ansMax))
    t-=1
'''
    Failed testcase 

    1
    4
    8 1 4 0
    My answer
    3 4 
    Correct Answer
    4 4
'''
