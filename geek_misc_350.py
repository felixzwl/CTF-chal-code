'''
xor1 = [0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44]
xor2 = [0xDA, 0x09, 0x2D, 0x76, 0x42, 0x5C, 0x29, 0x78, 0x53, 0x59, 0x63, 0x3C, 0x06, 0x1E, 0x77]
key = ''

for i in xrange(len(xor1)):
    key += chr(xor1[i] ^ xor2[i])
print key
'''
key = 'SYc1OV3r'
rd = open('d:/new.png', 'rb')
wt = open('d:/flag_png_new.png', 'wb')
r = rd.read()
strr = ''
loop = len(r)/len(key)
for i in xrange(len(r)):
    strr += chr(ord(r[i]) ^ ord(key[i % len(key)]))
wt.write(strr)
wt.close()
rd.close()