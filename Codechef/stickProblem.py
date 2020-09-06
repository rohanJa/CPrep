t=int(input())

while(t>0):
    s=int(input())
    l=list(map(int,input().split()))
    temp=set()
    for val in l:
        temp.add(val)
    
    if 0 in temp:
        print(len(temp)-1) 
    else:
        print(len(temp)) 

    t-=1 