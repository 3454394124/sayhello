#about file open, read, write

#wirte
with open('readme.txt', 'wt') as out_file:
    out_file.write('写写写进文档中\n的点点滴滴哒哒哒哒哒哒')

#read
with open('readme.txt', 'rt') as in_file:
    text = in_file.read()
print(text)