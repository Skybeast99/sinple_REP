def mulp_ab(a, b):
    '''перемножает a и b и печатает результат'''
    print(a * b)

def dev_ab(a, b):
    '''делит a на b и печатает результат'''
    if b == 0:
        print('на ноль делить нельзя')
    else:    
        print(a / b)

def sum_ab(a, b):
    '''складывает a и b и печатает результат''' 
    print(a + b)

def min_ab(a, b):
    '''вычитает из и печатает результат''' 
    print(a, b)

a = int(input('введите a '))
operation = (input('введите операцию '))
b = int(input('введите b '))
if operation == '+':
    sum_ab(a, b)
elif operation == '-':
    min_ab(a, b)
elif operation == '*':
    mulp_ab(a, b)
elif operation == '/':
    dev_ab(a, b)
else:
    print('вы не правельно ввели')
