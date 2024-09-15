print('### CASE 1 ###')
num1 = 11
num2 = num1

print('Before num2 value is updated:')
print(f'num1: {num1}')
print(f'num2: {num2}')

print(f'\nnum1 points to: {id(num1)}')
print(f'num2 points to: {id(num2)}')

num2 = 22

print('\nAfter num2 value is updated:')
print(f'num1: {num1}')
print(f'num2: {num2}')

# Reason: intergers are immutable (they can't be changed), so when we update num2, a new memory location is created for num2
print(f'\nnum1 points to: {id(num1)}')
print(f'num2 points to: {id(num2)}')

# ---------------------------------------------------

print('\n\n### CASE 2 ###')
num3 = 33
num4 = 33

print(f'num3 points to: {id(num3)}')
print(f'num4 points to: {id(num4)}')

# ---------------------------------------------------

print('\n\n### CASE 3 ###')
dict1 = {'value': 11}
dict2 = dict1

print('Before dict2 value is updated:')
print(f'dict1: {dict1}')
print(f'dict2: {dict2}')

print(f'\ndict1 points to: {id(dict1)}')
print(f'dict2 points to: {id(dict2)}')

dict2['value'] = 22

print('\nAfter dict2 value is updated:')
print(f'dict1: {dict1}')
print(f'dict2: {dict2}')

# Reason: dictionaries are mutable (they can be changed), so when we update dict2, dict1 is also updated
print(f'\ndict1 points to: {id(dict1)}')
print(f'dict2 points to: {id(dict2)}')

# ---------------------------------------------------

print('\n\n### CASE 4 ###')
dict3 = {'value': 33}
dict4 = {'value': 33}

print(f'dict3 points to: {id(dict3)}')
print(f'dict4 points to: {id(dict4)}')

# NOTE: if you don't have any variables pointing to a dictionary - you don't have any way to access that dictionary. In this case the dictionary will be garbage collected
