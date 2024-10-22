numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i = 4
count = len(numbers)
sum_ = sum(numbers[:i]) + sum(numbers[i + 1:])
average = sum_ / count
numbers[i] = average

print("Измененный список:", numbers)
