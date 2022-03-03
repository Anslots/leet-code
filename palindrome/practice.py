
x = 1237
str_x = str(x)
print(f'str_x is {str_x}')
print('str_x length is', len(str_x))
print('does str_x end with 37?', str_x.endswith('37'))
first_half_of_x = '1237'[0:2]
print(f'first half of str_x is {first_half_of_x}')
reverse_first_half_of_x = first_half_of_x[::-1]
print(f'reverse of first half of str_x is {reverse_first_half_of_x}')
