lst = [103, 107, 124, 119, 106, 109, 123, 125, 69, 73, 91, 82, 82, 97, 89, 76, 91, 95, 74, 67]
flag = ''

for i in lst:
    flag += chr(i ^ 62)

print flag