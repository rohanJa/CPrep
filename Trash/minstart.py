# takiong input array

arr=list(map(int,input().split()))

s=arr[0]
low=arr[0]


for i in range(1,len(arr)):
    s+=arr[i]
    if(low>s):
        low=s
print(-(low)+1)


