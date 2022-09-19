class Animal:
    def breathe(self):
        print("I am breathing")
    def eat(self):
        print("I am eating")
    def sleep(self):
        print("I am sleeping")
    def breed(self):
        print("I am breeding")

class Fish(Animal):
    def swim(self):
        print("I am swimming")

class Bird(Animal):
    def fly(self):
        print("I am flying")
    def walk(self):
        print("I am walking")

class Person(Animal):
    def walk(self):
        print("I am walking")

nemoFish = Fish()
brendaBird = Bird()
david = Person()
david.breathe()
brendaBird.breathe()
nemoFish.breathe()
