class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} is barking.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} the {self.color} cat is meowing.")
```

```python
# Dog instanssi yaratish
dog = Dog("Bobi", 3, "Golden Retriever")
dog.eat()
dog.sleep()
dog.bark()

# Cat instanssi yaratish
cat = Cat("Masha", 2, "Black")
cat.eat()
cat.sleep()
cat.meow()
