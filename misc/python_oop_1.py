class Dog():
    def __init__(self, name, age):
        self.name = name

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


d = Dog("Szymon", 10)
d.bark()
