# What is used to check whether an object o is an instance of class
# A?


# What is used to check whether an object o is an instance of class
# A?
class Animal:
    pass

class Dog(Animal):
    pass

dog1 = Dog()
animal1 = Animal()

# Check instances
print(isinstance(dog1, Dog))       # True
print(isinstance(dog1, Animal))    # True, because Dog is a subclass of Animal
print(isinstance(animal1, Dog))    # False
