from os import system
system("cls")

def intToRoman(num: int) -> str:
    r = ''
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    while num > 0:
        if num >= numbers[i]:
            num -= numbers[i]
            r += letters[i]
        else:
            i += 1
    return r

print(intToRoman(49))

# C = 100
# XC = 90
# L = 100