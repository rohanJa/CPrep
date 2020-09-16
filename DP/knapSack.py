wieght=list(map(int,input().split()))
val=list(map(int,input().split()))
cap=int(input())

DP = [[0 for j in range(0,cap+1)] for i in range(0,len(wieght)+1) ]

for i in range(1,len(wieght)+1):    #Looping through every wieght
    for j in range(1,cap+1):        #Uptil the capacity
        if(wieght[i-1]<=cap):
            DP[i][j]=max(val[i-1]+DP[i-1][j-wieght[i-1]],DP[i-1][j])
        else:
            DP[i][j]=DP[i-1][j]

# Array output
'''
for i in range(1,len(wieght)+1):
    for j in range(1,cap+1):
        print(DP[i][j],end=' ')
    print()
'''
ans=[]
res=DP[len(wieght)][cap]

print("Wieght ",end='')
for j in range(len(wieght),-1,-1):
        if(res==DP[j-1][cap]):
            continue
        else:
            res-=val[j-1]
            cap-=wieght[j-1]
            print("capacity "+str(cap))
            print(wieght[j-1],end=' ')
print("Max Value of Knapsack"+str(DP[len(wieght)][cap]))