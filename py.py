# Union-Find
from collections import defaultdict
# さいしょうぜんいきき
# https://qiita.com/uniTM/items/a6c5211ce9c9008b74a8#%E3%82%B3%E3%83%BC%E3%83%89%E4%BE%8B%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB%E6%B3%95

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

# Code

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    uf = UnionFind(n)
  
    edges = []
    index = 2
    
    for _ in range(n - 1):
        a = int(data[index]) - 1
        b = int(data[index + 1]) - 1
        c = int(data[index + 2])
        edges.append((c, a, b))
        index += 3

    queries = []
    for _ in range(q):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        w = int(data[index + 2])
        queries.append((w, u, v))
        index += 3

    def saisyouznniki(edges):
        uf = UnionFind(n)
        mst_weight = 0
        # 重みが小さい順に辺をソート
        edges.sort()
        for c, u, v in edges:
            if not uf.same(u, v):
                
                mst_weight += c# 重みを足し
                uf.union(u, v)# 頂点同士をつなげる
        return mst_weight

    mst_weight = saisyouznniki(edges)

    for w, u, v in queries:
        edges.append((w, u, v))
        mst_weight = saisyouznniki(edges)
        print(mst_weight)

if __name__ == '__main__':
    main()



