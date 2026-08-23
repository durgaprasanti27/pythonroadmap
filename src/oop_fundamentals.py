# OOP Fundamentals (Phase 2)

## Core Concepts
```python
# Classes & Objects
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

# Inheritance
class Dog(Animal):
    def speak(self):
        return f'Woof! I'm {self.name}'

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
```

## Key Principles
- Encapsulation: Hide internal state
- Inheritance: Reuse parent class behavior
- Polymorphism: Different objects respond to same method calls

## Exercises
1. Create a `Cat` class that inherits from `Animal`
2. Add a ` espectáculo` method to `Dog`
3. Demonstrate data hiding with `BankAccount`

**Goal**: Master OOP basics to build maintainable AI systems