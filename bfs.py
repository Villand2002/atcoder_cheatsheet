from collections import deque
import sys
input = sys.stdin.read

# 入力を受け取る
data = input().split()
N, M = map(int, data[:2])
graph = [[] for _ in range(N + 1)]
index = 2

# 道路情報をグラフに追加
for _ in range(M):
    A, B = map(int, data[index:index+2])
    graph[A].append(B)
    index += 2

count = 0

# 各都市からの到達可能都市をBFSで探索
for start in range(1, N + 1):
    visited = [False] * (N + 1)  # この都市固有の訪問記録
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 到達可能な都市のペアをカウント

print(count + N)  # 各都市から自身への到達（(i, i)）もカウントする
