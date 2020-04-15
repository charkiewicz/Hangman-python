number = int(input())

factorial = 1
counter = 1
while counter <= number:
    factorial *= counter
    counter += 1
print(factorial)
