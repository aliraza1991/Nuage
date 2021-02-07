import sys
file = sys.argv[1]

encrypt_word = ''
with open(file, 'r') as f:
	lines = f.readlines()
	for line in lines:
		for l in line:
			if ord(l) >= 65 and ord(l) <= 90:
				val = chr(65+(90-ord(l)))
				encrypt_word += val
			elif ord(l) >= 97 and ord(l) <= 122:
				val = chr(97+(122-ord(l)))
				encrypt_word += val
			else:
				encrypt_word += l
# print(encrypt_word)
with open('result.txt', 'w') as fb:
	fb.writelines(encrypt_word)
