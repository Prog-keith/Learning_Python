def add(a,b):
    return a + b 
def sub(a,b):
    return a - b 
def mul(a,b):
    return a * b 
def div(a,b):
    return a / b   


def get_function(operator='+'):

    if operator == "+":
        return add
    if operator == '-':
        return sub   
    if operator == '*':
        return mul
    if operator =='/':
        return div      

func = get_function() 

calc_dictionary = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div

}

print(func(3,4))

func = calc_dictionary['*']

print(func(3,4))

print(calc_dictionary['*'](100,3))

func = calc_dictionary['/']
print(func(30,3))


