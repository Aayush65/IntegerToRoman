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

if __name__ == "__main__":
    print(intToRoman(49))
