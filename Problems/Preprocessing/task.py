raw_input = input()
result = raw_input.replace(',', '').replace('.', '').replace('?', '').replace('!', '').lower()
print(result)