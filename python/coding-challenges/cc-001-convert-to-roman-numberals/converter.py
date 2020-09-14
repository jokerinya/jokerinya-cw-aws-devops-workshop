while True:
    num = input('''###  This program converts decimal numbers to Roman Numerals ###
(To exit the program, please type "exit")
Please enter a number between 1 and 3999, inclusively : ''')
    if num.lower() == 'exit':
        print("Goodbye")
        break
    elif num.isdecimal():
        num = int(num)
        if not 0 < num < 4000:
            print("Enter a number 0 < num < 4000: ")
        else:
            integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            roman = ["M", "CM", "D", "CD", "C", "XC",
                     "L", "XL", "X", "IX", "V", "IV", "I"]
            roman_num = ''
            x = 0
            while num > 0:
                for i in range(num // integer[x]):
                    roman_num += roman[x]
                    num -= integer[x]
                x += 1
            print(roman_num)