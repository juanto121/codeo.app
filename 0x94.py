n = int(input())
s_arr = input().split(" ")
arr = [int(v) for v in s_arr]

overall_max = arr[0]
max_so_far_including_item = 0

for val in arr:
	max_so_far_including_item = max( max_so_far_including_item + val, val)
	if max_so_far_including_item > overall_max:
		overall_max = max_so_far_including_item


print(overall_max)