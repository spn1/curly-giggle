class Parrot:
    def __init__(self, name, age):
        self.species = 'bird'
        self.name = name
        self.age = age

    def sing(self, song):
        print('{} is singing the song {}'.format(self.name, song))

polly = Parrot('Polly', 15)

polly.sing('Something Stupid')

# Inheritance
class Bird:
    def __init__(self):
        print('Bird Created')

    def who(self):
        print('I am a Bird')

    def swim(self):
        print('Going for a swim as a Bird')

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print('Penguin Created')

    def who(self):
        super().who();
        print('Penguin')

    def swim(self):
        print('Going for a swim as a Penguin')

peng = Penguin()
peng.who()
peng.swim()

# Encapsulation
class Computer:
    def __init__(self, max_price):
        # Variables with an underscore prefix are classes as private - they are not accessible from outside the class
        self.__max_price = max_price
        print('Computer Created');

    def sell(self):
        print('Selling computer for {}'.format(self.__max_price))

dell = Computer(100);
dell.sell();
dell.__max_price = 200
dell.sell();

print(dir(Penguin))