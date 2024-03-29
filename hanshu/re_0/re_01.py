import re

# 1.正则表达式 是一个特殊的字符序列，一个字符串是否与我们所设定的这样的字符序列，相匹配
# 快速检索文本、实现替换文本的操作
a='C|C++|Java|C#||Python|Javascript'

r = re.findall('Python',a)
print(r)

if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')
print('----------------------')
#2.元字符与普通字符
a='python 11\t11 java &678p\nh\rp php pytho 0python 1pythonn'
r = re.findall('\d',a)   #\d匹配一个数字字符。等价于 [0-9]。
f = re.findall('\D',a)   #\D匹配一个非数字字符。等价于 [^0-9]
z = re.findall('\s',a)    #\s  空白字符  \S
x = re.findall('\w',a)    #\w  数字和字母 =[a-zA-Z0-9_]  \W
w = re.findall('[a-z]{3,6}',a)   #数量词--- 打印字符串a-z，长度是3-6     贪婪模式
p = re.findall('[a-z]{3,6}?',a)   #非贪婪模式
t = re.findall('python*',a)      #* 匹配0次或者无限多次
o = re.findall('python+',a)       #+ 匹配1次或者无限多次
l = re.findall('python?',a)      # ? 匹配0次或者1次
print("匹配一个数字字符:"+str(r))
print("匹配一个非数字字符:"+str(f))
print("空白字符:"+str(z))
print("数字和字母:"+str(x))
print("这是贪婪模式，数量词3-6："+str(w))
print("这是非贪婪模式，数量词3-6："+str(p))
print("* 匹配0次或者无限多次"+str(t))
print("+ 匹配1次或者无限多次"+str(o))
print(l)
b = ''
for x in a:
    try:
        int(x)
        b += x+','
    except :
        pass
print(b)
print('----------------------------')

#3.找出中间一个字符不是C 和F的 单词
s = 'abc, acc, adc, aec, afc, ahc'
r = re.findall('a[^cf]c',s)    #[a-z] [cf]
print(r)
b = ''
for x in s:
    try:
        str(x)
        b += x+''
    except:
        pass
print("找出中间一个字符不是C 和F的 单词:"+str(b))
print("--------==================================")

# re.match函数   re.match(pattern（匹配的正则表达式）, string（要匹配的字符串）, flags=0)标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none
#我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
#group(num=0)       匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组
#groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('ru', 'runoob.com').span())         # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)



print(matchObj)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1,2))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
print("+++++++++++++++++++")
if matchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1,2))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("No search!!")

print("-----------===================")

# re.search方法       扫描整个字符串并返回第一个成功的匹配
# re.search(pattern, string, flags=0)    匹配成功re.search方法返回一个匹配的对象，否则返回None
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配




# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配
# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*	匹配0个或多个的表达式。
# re+	匹配1个或多个的表达式。
# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}	匹配n个前面表达式。例如，"o{2}"不能匹配"Bob"中的"o"，但是能匹配"food"中的两个o。
# re{ n,}	精确匹配n个前面表达式。例如，"o{2,}"不能匹配"Bob"中的"o"，但能匹配"foooood"中的所有o。"o{1,}"等价于"o+"。"o{0,}"则等价于"o*"。
# re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	匹配a或b
# (re)	匹配括号内的表达式，也表示一个组
# (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)	类似 (...), 但是不表示一个组
# (?imx: re)	在括号中使用i, m, 或 x 可选标志
# (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
# (?#...)	注释.
# (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功。
# (?> re)	匹配的独立模式，省去回溯。
# \w	匹配数字字母下划线
# \W	匹配非数字字母下划线
# \s	匹配任意空白字符，等价于 [\t\n\r\f]。
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9]。
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置。
# \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等。	匹配一个换行符。匹配一个制表符, 等
# \1...\9	匹配第n个分组的内容。
# \10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。