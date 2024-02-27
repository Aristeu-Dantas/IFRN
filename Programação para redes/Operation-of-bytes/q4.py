# Remember the algorithm that changes the base? Make a program that receives a
# decimal integer and shows that number in base 6.

decimal_number = int(input("Enter a decimal number: "))

def decimal_to_base6(enter):
    if enter == 0:
        return "0"
    base6_digits = []
    while enter > 0:
        remainder = enter % 6
        base6_digits.append(str(remainder))
        enter //= 6
    base6_digits.reverse()
    base6_str = "".join(base6_digits)
    return base6_str

base6_representation = decimal_to_base6(decimal_number)

print(f"The number {decimal_number} in base 6 is: {base6_representation}")
