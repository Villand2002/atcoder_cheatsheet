# キーでソート
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_by_keys = dict(sorted(my_dict.items()))
print(sorted_by_keys)
# 出力: {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}

# 値でソート
my_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_values)
# 出力: {'pear': 1, 'orange': 2, 'banana': 3, 'apple': 4}


# 二重リストのソート
my_list = [[1, 3], [4, 1], [2, 2], [3, 4]]

# 2番目の要素でソート
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)
# 出力: [[4, 1], [2, 2], [1, 3], [3, 4]]


# 二重リストの複数の列でのソート
my_list = [[1, 3], [4, 1], [2, 2], [3, 4], [1, 2]]

# 最初の列でソートし、次に2番目の列でソート
sorted_list = sorted(my_list, key=lambda x: (x[0], x[1]))
print(sorted_list)
# 出力: [[1, 2], [1, 3], [2, 2], [3, 4], [4, 1]]



from collections import defaultdict

# デフォルト値が0のdefaultdictを作成
int_default_dict = defaultdict(int)

# 存在しないキーにアクセスすると0が返される
print(int_default_dict['key1'])  # 出力: 0

# 値を追加
int_default_dict['key1'] += 1
print(int_default_dict['key1'])  # 出力: 1



# デフォルト値が空リストのdefaultdictを作成
list_default_dict = defaultdict(list)

# 存在しないキーにアクセスすると空リストが返される
print(list_default_dict['key1'])  # 出力: []

# リストに値を追加
list_default_dict['key1'].append(1)
print(list_default_dict['key1'])  # 出力: [1]
