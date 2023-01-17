def new_line():
    print('.')

def three_lines():
    new_line()
    new_line()
    new_line()

def nine_lines():
    three_lines()
    three_lines()
    three_lines()

def clearScreen():
    print('Print nine lines')
    nine_lines()
    print('Print three lines')
    three_lines()
    print('Print nine lines')
    nine_lines()
    print('Print three lines')
    three_lines()
    print('Print new line')
    new_line()

print('Printing Line from main function')
print('Calling clearScreen')
clearScreen()
