import math

def calculator():
    while True:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

        operation = raw_input('Enter the operation (+, -, *, /, sqrt, pow, sin, cos, tan, log, log10): ')

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print('Error: Division by zero is not allowed')
                continue
            result = num1 / num2
        elif operation == 'sqrt':
            result = math.sqrt(num1)
        elif operation == 'pow':
            result = math.pow(num1, num2)
        elif operation == 'sin':
            result = math.sin(num1)
        elif operation == 'cos':
            result = math.cos(num1)
        elif operation == 'tan':
            result = math.tan(num1)
        elif operation == 'log':
            result = math.log(num1)
        elif operation == 'log10':
            result = math.log10(num1)
        else:
            print('Invalid operation! Please enter a valid operation.')
            continue

        print('Result: {} {} {} = {}'.format(num1, operation, num2, result))

        choice = raw_input('Do another calculation (yes/no): ')
        if choice.lower() != 'yes':
            print('THANK YOU FOR TESTING!!!')
            break

calculator()