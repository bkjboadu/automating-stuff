
def collatz(number):
    if number % 2 == 0:
        value = number // 2
        print(value)
        return value
    elif number % 2 == 1:
        value = 3 * number + 1
        print(value)
        return value


number = input('Enter number:')
number = int(number)

try:
    result = collatz(number)
    while result != 1:
        result = collatz(result)
        result
except ValueError:
    print('Please enter an integer')











