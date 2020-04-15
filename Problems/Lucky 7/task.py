counter = int(input())
squares = []
for i in range(counter):
    tmp = int(input())
    if tmp % 7 == 0:
        squares.append(tmp*tmp)

for square in squares:
    print(square)
