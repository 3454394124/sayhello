#使用递归实现斐波那契数列

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n - 1) + recur_fibo(n - 2))

n = int(input('请输入需要的项数：'))

if n <= 0:
    print('您的输入有误')
else:
    print('斐波那契数列为：')
    for i in range(0, n):
        print(recur_fibo(i))