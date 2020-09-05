str1=input()
str2=input()

DP=[[0 for i in range(0,len(str1)+1)] for j in range(0,len(str2)+1)]
result=-1
for i in range(1,len(str2)+1):
    for j in range(1,len(str1)+1):
        if(str2[i-1]==str1[j-1]):
            DP[i][j]+=DP[i-1][j-1]+1
        else:
            DP[i][j]=0
        result=max(DP[i][j],result)
print(result)