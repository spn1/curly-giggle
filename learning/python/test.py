print('Hello World')

a = 3
b = 4

c = a + b
print(c)

# Multiline code
d = a + a + a + a \
  + b + b + b + b \
    + a

e = {a + b + c + a 
  + b + c}

f = [a + b + d + d]
print(d)
print(e)
print(f)

# Code blocks are defined with indentation
for i in range(1,11):
    print(i)
    if i == 5:
        break

'''
Triple quotes / apostrophes can 
be used for multi-line
comments
'''

# Docstrings - A way of documenting the purpose of a function
# use """ string """ to define a docstring immediately after declaring the function

def double(number):
  """doubles a number"""
  return 2 * number

print(double(210))
print(double.__doc__)

import constants

print(constants.PI)
print(constants.EARTH_GRAVITY)

# None is undefined / null
undefined = None
print(undefined)

# Four types of collections
# Array
fruit = ['Apple', 'Banana', 'Mango', 'Persimmon', 'Strawberry', 'Tomato']
print(fruit)

for thing in fruit:
  print(thing)

print(fruit[2:4])
print(fruit[3:])

# Tuple - An Immutable Array
numbers = ('one', 'two', 'three', 'four', 'five', 'six')
# can't do this: numbers[0] = 'test'

# Set - an unordered list of UNIQUE items - cannot add duplicates
# cannot access by index, since it is unordered
fruit_i_bought = { 'apple', 'apple', 'banana', 'mango', 'persimmon', 'persimmon', 'persimmon'}
print(fruit_i_bought)
for f in fruit_i_bought:
  print(f)

# Dictionary - key-value pairs - optimized for retrieving data 
fruit_prices = {
  'apple': 1.5,
  'mango': 2.00,
  'persimmon': '???',
  'banana': True
}
print(fruit_prices)
print(fruit_prices['banana'])

# Print has some additional functions: 
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
# print(1, 2, 3, 4, sep='#', end='&')

# Variable Substitution
firstname='Spencer'
lastname='Newton'
print('I love {}s and {}s'.format(fruit[0], fruit[1]))
print('Greetings {name}, how are you today?'.format(name=firstname))

# User Input
# num = input('Enter a Number: ')

if (fruit[0] is 'Apple'): print('is Apply');
if (fruit[0] is not 'Banana'): print('is not banana');
if ('Apple' in fruit): print('contains apple');

print('Memory Address of fruit: ', id(fruit));

# if elif else
# userinput=int(input('Enter Number: '));
# if (userinput > 0):
#     print('Greater Than Zero')
# elif (userinput is 0):
#     print('Is Zero');
# else:
#     print('Less Than Zero')

# Else can be used at the end of a for loop to do something right at the end OR if can't be found
print('The fruid I want to buy are: ')
for f in fruit:
    print(f)
else:
    print('I will go buy them now :)')