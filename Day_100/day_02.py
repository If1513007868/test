print('-------------------循环结构------------------------')
print('-------------------在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环。------------------------')
print('1.----------------------计算1~100求和的结果--------------------------')
sum = 0
for x in range(1,101):
    sum += x
print(sum)
print('2.----------------------用for循环实现1~100之间的偶数求和--------------------------')
sum = 0
for x in range(1,101,2):   #range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量
    sum += x
print(sum)

print('''
也可以通过在循环中使用分支结构的方式来实现相同的功能，
sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)
''')
print('----------------------如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环--------------------------')
print('''while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True循环继续，表达式的值为False循环结束''')
# import random
# answer = random.randint(1,10)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入: '))
#     if number <answer:
#         print('大一点')
#     elif number > answer:
#         print('小一点')
#     else:
#         print('恭喜你猜对了!')
#         break
# print('你总共猜了%d次'%counter)
# if counter <7:
#     print('你的智商余额明显不足')

for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(i,j,i*j),end=' ')
    print()
print('3.----------------------打印如下所示的三角形图案---------------------------------------')
row = int(input('请输入行数: '))
for i in range(row):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

for i in range(row):
    for j in range(row):
        if j < row -i -1:
            print(' ',end=' ')
        else:
            print('*', end=' ')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()

