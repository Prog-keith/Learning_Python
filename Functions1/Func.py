
def add(a,b):
    return a + b 
def sub(a,b):
    return a - b 
def mul(a,b):
    return a * b 
def div(a,b):
    return a / b



calc_dictionary = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div

}


print(calc_dictionary['*'](100,3))