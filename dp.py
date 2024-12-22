# knackpack problem
N,W=map(int,input().split())

dp=[[0]*(W+1)]*(N+1)

graph=[]

for i in range(N):
    w,v=map(int,input().split())
    graph[i].append([w,v])
    
for i in range(1,N+1):
    for j in range(1,W+1):
        if graph[i-1][0]<=j:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-graph[i-1][0]]+graph[i-1][1])
        else:
            dp[i][j]=dp[i-1][j]    
    
print(dp[N][W])


mod=1000000007


N,M=map(int,input().split())

break=[]

for i in range(M):
    a=int(input())
    break.append(a)