numbers = [int(x) for x in input().split()]

sum = 0
for number in numbers:
    sum += number
mean = sum / len(numbers)
print(mean)