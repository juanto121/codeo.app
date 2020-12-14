s = input()

table = [0] * len(s)

i = 0
j = i + 1

while i < len(s) and j < len(s):
	if s[i] != s[j]:
		if i != 0:
			i = table[i-1]
			continue
		table[j] = 0
		j += 1
	else:
		table[j] = i + 1
		i += 1	
		j += 1

print(table[len(s)-1])
