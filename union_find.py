# UnionFind
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
 
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
 
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return 
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
        return 
 
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
 
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
 
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]



# ・初期化：変数名=UnionFind(要素の数)
# ・グループリーダー(根)の確認：変数名.leader(要素番号)
# ・グループ化：変数名.merge(要素番号1,要素番号2)
# ・同一グループかの確認：変数名.same(要素番号1,要素番号2)
# 　(同一ならTrue,違うグループならFalseを返す)
# ・所属するグループのサイズ確認：変数名.size(要素番号)
# ・グループ全体の確認：変数名.groups()


# 初期化：変数名=UnionFind(要素の数)
UF=UnionFind(10)

# グループ化：変数名.merge(要素番号1,要素番号2)
UF.merge(0,2)
UF.merge(1,3)
UF.merge(3,0)

# グループリーダー(根)の確認：変数名.leader(要素番号)
leader_x=UF.leader(1)

# 同一グループかの確認：変数名.same(要素番号1,要素番号2)
if UF.same(1,5)==True:
    print("同一グループ")
else:
    print("別グループ")

# 所属するグループのサイズ確認：変数名.size(要素番号)
size_x=UF.size(1)

# グループ全体の確認：変数名.groups()
print(UF.groups())



from collections import defaultdict


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

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
        


# n個の要素を0 ~ n - 1の番号で管理する。以下の属性およびメソッドを持つ。

# parents
# 各要素の親要素の番号を格納するリスト
# 要素が根（ルート）の場合は-(そのグループの要素数)を格納する
# find(x)
# 要素xが属するグループの根を返す
# union(x, y)
# 要素xが属するグループと要素yが属するグループとを併合する
# size(x)
# 要素xが属するグループのサイズ（要素数）を返す
# same(x, y)
# 要素x, yが同じグループに属するかどうかを返す
# members(x)
# 要素xが属するグループに属する要素をリストで返す
# 関連記事: Pythonリスト内包表記の使い方
# その後に行う処理によっては集合内包表記やジェネレータ式を使うほうが効率的かもしれない（下のroots()も同じ）
# roots()
# すべての根の要素をリストで返す
# group_count()
# グループの数を返す
# all_group_members
# {ルート要素: [そのグループに含まれる要素のリスト], ...}のdefaultdictを返す
# defaultdictは辞書dictのサブクラス
# collections - defaultdict --- コンテナデータ型 — Python 3.9.0 ドキュメント
# __str__()
# print()での表示用
# ルート要素: [そのグループに含まれる要素のリスト]を文字列で返す
# f文字列を利用している