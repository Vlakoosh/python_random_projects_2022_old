class Pet():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show_self(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Cat(Pet):
    def speak(self):
        print("meow")

class Dog(Pet):  
    def speak(self):
        print("bark")