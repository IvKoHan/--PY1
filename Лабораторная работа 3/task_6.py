list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = list_numbers[0]
index = 0

for i in range(1, len(list_numbers)):
    if max_num <= list_numbers[i]:
        max_num = list_numbers[i]
        index = i

num = list_numbers[-1]
list_numbers[-1] = max_num
list_numbers[index] = num

print(list_numbers)
