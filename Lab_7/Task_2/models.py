class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        return "Some generic animal sound"

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}"

    def __str__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, color={self.color})"


class Dog(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

    def info(self):
        return f"{super().info()}, Breed: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, color, indoor):
        super().__init__(name, age, color)
        self.indoor = indoor

    def speak(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the sofa."

    def info(self):
        return f"{super().info()}, Indoor: {self.indoor}"