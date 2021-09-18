def comma_code(args):
    if len(args) == 0:
        return []
    else:
        till_and_string = str(', '.join(args[0:len(args) - 1]))
        print(till_and_string + ', and ' + args[len(args) - 1])


spam = ['apples', 'bananas', 'tofu', 'cats','cow','meat','animal']


comma_code(spam)

