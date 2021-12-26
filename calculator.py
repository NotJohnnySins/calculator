while True:
    type1 = input('Addittion: + | Subtraction: - | Multiplication * | Division / | q To stop| ')
    if type1 == "+":
        num1 = int(input('Write a number '))
        num2 = int(input('Write a second number '))
        if num1 and num2:
            print(f"{num1} + {num2} = {num1 + num2}")
    if type1 == "-":
        num1 = int(input('Write a number '))
        num2 = int(input('Write a second number '))
        if num1 and num2:
            print(f"{num1} - {num2} = {num1 - num2}")
    if type1 == "*":
        num1 = int(input('Write a number '))
        num2 = int(input('Write a second number '))
        if num1 and num2:
            print(f"{num1} * {num2} = {num1 * num2}")
    if type1 == "/":
        num1 = int(input('Write a number '))
        num2 = int(input('Write a second number '))
        if num1 and num2:
            print(f"{num1} / {num2} = {num1 / num2}")
        print(f"{num1}")
    if type1 == "q":
        exit()