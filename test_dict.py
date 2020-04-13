point = {'x': 1, 'y': 2}
# 打印字典的类型dict
print(type(point))

# 初始化字典
book = {'name': 'Java', 'age': 25}
print(book)

# 增加字典属性key-value
book['no'] = 1

# 删除字典中的key
del book['age']
print(book)

# 访问字典的key
print(book['name'])

# 利用字典统计词频
freq = {}
word = 'professional'
for c in word:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
for key in freq.keys():
    print('字母%s出现次数: %d' % (key, freq[key]))

