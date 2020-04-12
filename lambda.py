# lambda表达式
a = (1, 3, 4, 5)

# filter过滤器
# list把结果转成列表
b = list(filter(lambda x: x < 4, a))
print(b, type(b), len(b))
