# A base ten element has ten possible values, from zero to nine.
# a) Each element in base sixteen has how many possible values?
#b) Base 62 has 62 different elements. Suppose the elements in that
# base are: 0, 1, 2, ...., 9, a, b, c, ....z, A, B, C, D, .... Z. In this scenario the letter a
# represents the value 10, b o 11, .... , z o 35, A o 36, B o 37, until finally Z
# which represents 61. What is the value in base 10 of the following elements in base
#62:
# •a3
# •A3
# •51z
# •100

print('a) In base 16 there are 16 possible values.')

def convert_function(x):
    base62="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base10=0
    for y in x:
        base10=base62.index(y)+62*base10
    return base10

print(convert_function('a3'))
print(convert_function('A3'))
print(convert_function('51z'))
print(convert_function('100'))
