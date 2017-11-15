a = 'I Love Python'
print(a[0:12])
print(a[-13:-1])
print(a[:-1])
print(a[-3:-10])    # 不管正负，只能，从左到右。

# 分隔符的使用

a = 'www.baidu.com'
print(a.split('.'))

a = 'www-baidu-com'
print(a.split('-'))

a = 'www baidu com'
print(a.split())

print('\n')

# replace()方法

a = 'there is apples'
b = a.replace('is', 'are')
print(a)
print(b)

# strip()方法

a = '  Python is very cool  '
print(a.strip())                # 文本首尾去空格

a = '***Python *is  *very *good***'
print(a.strip('*'))             # 去除首尾指定字符

print('\n')

# format()方法

a = '{} is my best love.'.format('Python')
print(a)

# content = input('请输入搜索内容：')     # 如：yyPython
# url_path = 'http://www.cnblogs.com/{}/'.format(content)
# print(url_path)

print('\n')

# 函数应用(脏活累活全给函数，尤其计算)


def fun(a, b):
    return 1/2*a*b


s = fun(2, 3)
print(s)


def change_number(number):
    hiding_number = number.replace(number[3:7], '*'*4)
    print(hiding_number)


change_number('13264151343')

# 多重循环

names = ['承一', '熊二', '张三', '赵四']
age = [23, 15, 58, 36]

for names, age in zip(names, age):  # 这个zip()是个好东西
    print(names,age)

# 列表推导式

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(num) for num in range(1, 14)]
for url in urls:
    print(url)

print('\n')


# 打开并写入文件file.txt(文件事先不存在)(路径用"/")
f = open('C:/Users/Administrator/Desktop/file.txt', 'w')
f.write('hello python!')

# 读取文件
f = open('C:/Users/Administrator/Desktop/file.txt', 'r')
content = f.read()
print(content)

# 关闭文件

f = open('C:/Users/Administrator/Desktop/file.txt', 'r')
content = f.read()
print(content)
f.close()

print('\n')

# 类的继承


class Bike:
    compose = ['frame', 'wheel', 'pedal']   # 公共属性

    def __init__(self):                     # 附加属性
        self.other = 'basket'

    def use(self, time):
        print('you ride {}m'.format(time*100))


class ShareBike(Bike):                      # 共享单车类想用车类的属性或方法(此处需要用到属性)，就继承它好了
    def cost(self, hour):
        print('you cost {} yuan.'.format(hour*2))


bike = ShareBike()
print(bike.other)
bike.cost(2)
