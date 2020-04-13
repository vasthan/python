# # 输出
# # open -> write -> close
# file1 = open('book.txt', 'w', encoding='utf-8')
# file1.write('三国演义')
# file1.write('\n')
# file1.write('西游记')
# file1.close()
#
# # 输入
# # open -> read -> close
# file2 = open('book.txt', encoding='utf-8')
# content = file2.read()
# print(content)
# file2.close()
#
# # 追加写入模式
# file3 = open('book.txt', 'a', encoding='utf-8')
# file3.write('\n曹操')
# file3.close()

file4 = open('book.txt', encoding='utf-8')
for line in file4.readlines():
    print(line)
    print('-------------')

# seek和tell的单位是字节
# read读取的单位是字符
file4.seek(0)
print(file4.read(1))
print(file4.read(1))
print('当前偏移量：%d' % file4.tell())
file4.close()
