stdin = input().split(" ")

a = int(stdin[0])
b = int(stdin[1])

if (a == b):
	print("=")
else:
	print(">" if a > b else "<")