# An even more different base is base 256. There must be 256 possible
# symbols to represent each of its elements. How difficult can it be
# find this number of symbols, adopt the following criteria:
# 00 – represents zero in base 256
# 01 – represents 1 in base 256
# 02 – represents 2 in base 256
# 09 – represents 9 in base 256
# 0A – represents 10...
# 0B – represents 11
# ...
# 0F – represents 15
# 10 – represents 16
# 11 – represents 17
# ...
# 1A – represents 26
# ...
# 1F – represents 31
# 20 – represents 32
# ...
# 32 – represents 0 50
# A0 – represents 160
# ....
# FF – represents 255
# a) Following this pattern, try to find out which element in base 256 is
# represented by each of the following pairs:
# ▪pair 34 – represents element 52
# ▪pair 72 – represents _____
# ▪the 4C pair – represents the _____
# ▪the C2 pair – represents the _____
# ▪the F2 pair – represents the _____
# b) Considering that each of the pairs represents an element in base 256,
# Determine the value in base 10 of the following elements in base 256 (not
# forget to follow the pattern: the rightmost element (in this case, the pair) is
# multiplied by 2560, the next by 2561, the next by 2562 and so on
# against:
# ▪4C 32 – represents _____
# ▪72 F2 – represents _____
# ▪36 8A 25 – represents ______
# ▪33 78 54 D5 – represents the ______
# ▪08 00 00 00 – represents the _________

def convert_16_to_10(s):
    return int(s, 16)

def convert_256_to_10(s):
    base10 = 0
    for y in s:
        user = int(y, 16)
        base10 = base10 * 256 + user
    return base10

print('a)')
print(convert_16_to_10("34"))
print(convert_16_to_10("72"))
print(convert_16_to_10("4C"))
print(convert_16_to_10("C2"))
print(convert_16_to_10("F2"))
print("*"*10)
print('b)')
print(convert_256_to_10("00"))
print(convert_256_to_10("01"))
print(convert_256_to_10("09"))
print(convert_256_to_10("0A"))
print(convert_256_to_10("1F"))
print(convert_256_to_10("20"))
print(convert_256_to_10("FF"))
print(convert_256_to_10("A0"))
