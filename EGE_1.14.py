
x = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
s1 = '1x1x1x1x1'
s2 = '20x24'
s3 = '1x235'

for i in x:
    b1, b2, b3 = s1.replace('x', i), s2.replace('x', i), s3.replace('x', i)
    b1, b2, b3 = int(b1, 23), int(b2, 23), int(b3, 23)
    b = b1 + b2 + b3
    if b % 22 == 0:
        res = b / 22
        break

print(int(res))