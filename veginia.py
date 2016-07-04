from __future__ import print_function
import itertools

def ch63():
	#p = 'ATTACKATDAWN'
	#k = 'LEMON'
	#c = vigenere_encrypt(p, k)
	#print(c, vigenere_decrypt(c, k))
	c = 'KDERE2UNX1W1H96GYQNUSQT1KPGB'
	k = 'fselkladfklklakl'
	print(c, vigenere_decrypt(c, k))

def vigenere_encrypt(s, key):
	base, buf = ord('a'), []
	for a, b in zip(s.lower(), itertools.cycle(key.lower())):
		a1, b1 = ord(a) - base, ord(b) - base
		shift = (a1 + b1) % 26
		buf.append(chr(base + shift))
	return ''.join(buf)

def vigenere_decrypt(s, key):
	base, buf, c, l = ord('a'), [], 0, len(key)
	for i in range(0, len(s)):
		a1 = ord(s[i].lower()) - base
		if a1 < 0 or a1 > 25:
			buf.append(s[i])
		else:
			b1, c = ord(key[c % l].lower()) - base, c + 1
			shift = (a1 - b1) % 26
			buf.append(chr(base + shift))
	return ''.join(buf)

if __name__ == '__main__':
	ch63()
