#定义简单加减乘除函数
def add(x, y):
    return (x + y)

def subtract(x, y):
    return(x -y)

def multipy(x, y):
    return(x * y)

def devide(x, y):
    return(x / y)

print('请选择想要进行的运算：')
print('1.相加')
print('2.相减')
print('3.相乘')
print('4.相除')

i = int(input('请选择需要进行的运算：'))

num1 = float(input('请输入第一个数：'))
num2 = float(input('请输入第二个数：'))

if i == 1:
    print(num1, num2, '的和为：', add(num1, num2))
elif i == 2:
    print(num1, num2, '相减为：', subtract(num1, num2))
elif i == 3:
    print(num1, num2, '的积为：', multipy(num1, num2))
elif i == 4:
    print(num1, num2, '相除为：', devide(num1, num2))
else:
    print('请非法输入')