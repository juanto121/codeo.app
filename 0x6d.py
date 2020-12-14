n = int(input())
s_arr = input().split(" ")
arr = [int(v) for v in s_arr]

first = arr[0]
ordered = True

for item in arr[1:]:
	if item < first:
		ordered = False
		break
	first = item

print("Ordenado" if ordered else "Desordenado")
