t=int(input())

while(t>0):
    n=int(input())
    graph=[[0 for i in range(0,n)] for i in range(0,n)]
    te=0
    ver=[]
    for i in range(0,n-1):
        a,b = map(int,input().split())
        graph[a-1][b-1]=1
        ver.append(b)
        
        if(i==0):
            te=a-1
    # for i in range(0,n):
    #     for j in range(0,n):
    #         print(graph[i][j],end=" ")
    #     print()
    if(n-1==len(ver)):
        print(0)
    else:
        print(1))
    visited=[False for i in range(0,n)]
    count=0
    st=[te]
    while(len(st)):
        i=st.pop()
        print(i)
        for j in range(0,n):
            if(graph[i][j]):
                if(not visited[j]):
                    visited[j]=True
                    st.append(j)
                else:
                    count+=1
    print(count)

    t-=1