from collections import deque

cases = int(input())

for case in range(cases):
	n = input()
	buildings = [int(v) for v in input().split(" ")]
	
	result = []
	stack = deque([buildings[-1]])

	for building in buildings[::-1]:
			
		while len(stack) > 0 and building >= stack[-1]:
			stack.pop()

		if len(stack) > 0 and building < stack[-1]:
			result.insert(0, stack[-1])
		if len(stack) == 0:
			result.insert(0, -1)

		stack.append(building)

	str_result = ""
	for building in result:
		str_result += str(building) + " "

	print(f"Case #{case+1}: {str_result}")

