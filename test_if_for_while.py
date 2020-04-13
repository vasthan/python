import time

# year = int(input("请输入年份: "))
#
# if year == 2018:
#     print("你今年会发大财")
# else:
#     print("今年倒霉")


chars = "abcdefg"
# iterator迭代法
for c in chars:
    print(c)

# 按次数循环
for i in range(12):
    print(i)

# while循环，break和continue
cnt = 0
while cnt < 100:
    cnt += 1
    if cnt == 88:
        break
    if cnt == 5:
        continue
    print('运行了 %d 次' % cnt)
    time.sleep(1)


