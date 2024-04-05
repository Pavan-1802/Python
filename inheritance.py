class Pet():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self):
        print("I don't know what to say")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, colour):
        super().__init__(name,age)
        self.colour=colour

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am {self.colour} in colour")

    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

p=Pet("Tim",5)
c=Cat("Tom",12,"Brown")
d=Dog("Spike",14)
p.show()
p.speak()
c.show()
c.speak()
d.show()
d.speak()