# 序列数据结构，支持下标访问。包括字符串、列表、元组


# 1 字符串str
chars = "hello python"
print(chars[0], chars[-1], chars[-6:])

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
year = 2020
print(chinese_zodiac[year % 12])

print("狗" in chinese_zodiac)
print("Thinking" + " in Java")
print("Go" * 3)


# 2 列表list
# 列表存储的元素可以变更
books = ['CSAPP', 'Clean Code', 'Code Complete']
print(books)
books.append('Effective Java')
print(books)
books.remove('CSAPP')
print(books)

# 3 元组tuple
# 元组存储的元素不可变更
zodiac_names = ('魔羯座', '水瓶座', '双鱼组', '白羊座', '金牛座', '双子座',
                '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

(month, day) = (8, 17)
zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
zodiac_index = len(list(zodiac_day))
print(zodiac_names[zodiac_index % 12])
