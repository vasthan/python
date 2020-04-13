# 偶数的平方
square_numbers = []
for i in range(11):
    if i % 2 == 0:
        square_numbers.append(i * i)
print(square_numbers)

# 使用列表推导式简化代码，以声明的方式写代码，更优雅
sn = [i*i for i in range(11) if i % 2 == 0]
print(sn)

# 使用字典推导式初始化字典
lang = {c: 0 for c in ('Java', 'Python', 'Go', 'Scala')}
print(lang)
