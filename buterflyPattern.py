"""
BUTTERFLY PATTERN - USING PYTHON
CREATOR - UTPAL

"""



chars = ['*', ' ']
rows = 8

for i in range(rows//2):
	for j in range(rows):
		if j <= i or j >= (rows - 1) - i:
			print(chars[0], end='')
		else:
			print(chars[1], end='')
	print()
	
for i in range(rows//2-1, -1, -1):
	for j in range(rows):
		if j <= i or j >= (rows - 1) - i:
			print(chars[0], end='')
		else:
			print(chars[1], end='')
	print()