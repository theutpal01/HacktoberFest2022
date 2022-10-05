
# Matrix Multiplication Program

def matrix_multiplication():
	for i in range(len(A)):
		for j in range(len(B[0])):
			for k in range(len(B)):
				res[i][j] += A[i][k] * B[k][j]

A=[]
B=[]

print("Enter N:")
n = int(input())

print("Enter Matrix A:")
for i in range(0, n):
	temp = []
	for j in range(0, n):
		x = int(input())
		temp.append(x)
	A.append(temp)

print("Enter Matrix B:")
for i in range(0, n):
	temp = []
	for j in range(0, n):
		x = int(input())
		temp.append(x)
	B.append(temp)

res = []
for i in range(0, n):
	temp = []
	for j in range(0, n):
		temp.append(0)
	res.append(temp)

matrix_multiplication()

for r in res:
	print(r)
