str1=input()
str2=input()

DP=[[0 for i in range(0,len(str2)+1)] for j in range(0,len(str1)+1)]

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if(str1[i-1]==str2[j-1]):   
            DP[i][j]=DP[i-1][j-1]+1     #the diagonal cell as it just before cell of the current cell 
        else:
            DP[i][j]=max(DP[i][j-1],DP[i-1][j])     #left and the the above cell of the current cell

for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        print(DP[i][j],end=' ')
    print()
print(DP[len(str1)][len(str2)])