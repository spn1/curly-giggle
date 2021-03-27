def greet(name, greeting='Greetings'):
    """Prints a greeting for the specified name"""
    print('{greeting}, {person}'.format(person=name, greeting=greeting))

greet('Lanaya')
greet('Spencer', 'Sup homey');
greet(greeting='Welcome', name='Sponker')

def greetmany(*names):
    for name in names:
        print('How do you do, ', name)

greetmany('Spencer', 'Sponker', 'Spinker')

# Anonymous Functions are called 'lambda' functions - without a defined name - but they can be assigned to variables
double_num = lambda x: x * 2
print(double_num(5))

numbers=range(0, 10)
even_numbers=list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Global Vars
x = 'global var'

def foo():
    x = 2
    print(x)

print(x)
foo()
print(x)

def change_global_var():
    global x
    x = 'test'

change_global_var()
print(x)
