class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the overridden sound methods
print(dog.sound())  
print(cat.sound())   