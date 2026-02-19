class Animal:           # Parent/Base class
    def speak(self):
        print("Some sound")

class Dog(Animal):  
    pass
        # Dog inherits from Animal
class Cat(Animal):      # Cat inherits from Animal
    pass


# animals = [Dog(),Cat()]
# for a in animals:
#     a.speak()

class Cat(Animal):
   def speak(self):
        print("meon")
animals = [Dog(),Cat()]
for a in animals:
    a.speak()