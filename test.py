N,M=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque,defaultdict

que=deque()


que.append(1)

visited=set()

visited.add(1)s

dist=0

for i in range(N):
    min_dist=[float('inf') for _ in range(N+1)]
    min_dist[1]=0
    while que:
        current=que.popleft()
        dist+=1
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                que.append(neighbor)
                min_dist[neighbor]=min(min_dist,dist)
    print(min_dist)
                
n,k=map(int,input().split())
a=list(map(int,input().split()))
a=a.sort()
ok=0
ng=k
while abs(ok-ng)>1:
    mid = (ok+ng)//2
    if solve(mid):
        ok=mid
    else:
        ng=mid
        
print()

num=[0]*(N+1)

D,N=map(int,input().split())
for i in range(N):
    L,R=map(int,input().split())
    num[L:R]+=1

for i in range(D):
    print(num[i])
    
    
    
    
def count_overlapping_intervals(N, intervals):
    events = []
    
    for l, r in intervals:
        events.append((l, 1)) 
        events.append((r + 1, -1))  
    
    events.sort()
    
    current_intervals = 0
    total_count = 0
    
    for i in range(len(events)):
        point, event_type = events[i]
        current_intervals += event_type
        
        if event_type == 1:
            total_count += current_intervals - 1

    return total_count


data = input().split()

N = int(input())
intervals = 

# 結果を出力
print(count_overlapping_intervals(N, intervals))

N,Q=map(int,input().split())


T=defaultdict(1)

for i in range(Q):
    T[i]+=1
