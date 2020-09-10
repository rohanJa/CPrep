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
        slowSpeed=speed[val]
        for j in range(0,len(speed)):
            if(j!=val):
                if(val>j and speed[j]>speed[val]):
                    resultMax+=1
                    if fastSpeed==speed[val]:
                        fastSpeed=speed[j]
                    else:     
                        fastSpeed=max(fastSpeed,speed[j])

                elif(val<j and speed[j]<fastSpeed):
                    if slowSpeed==speed[val]:
                        slowSpeed=speed[j]
                    else:     
                        slowSpeed=min(slowSpeed,speed[j])
        
                    resultMax+=1

        #people behind the current selected player which are slower than the speed of selected player 
        # can get infected if the current player infects a player which is slower than him.Then the 
        # slow player will infect the player behind the selected player which are faster than the player which 
        # are ahead then the selected player (i.e.) in position but solwer in speed.  

        for j in range(0,val):
            if slowSpeed!=speed[j] and speed[j]<=speed[val]:
                if speed[j]>slowSpeed:
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
