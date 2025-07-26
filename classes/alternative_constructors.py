class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person_from_birth_year(cls, name, birth_year):
        age = cls.calculate_age(birth_year)
        return cls(name, age)

    @staticmethod
    def calculate_age(birth_year):
        current_year = 2024  # Replace with the actual current year
        return current_year - birth_year

# Using the regular constructor
person1 = Person("Alice", 30)
print(f"{person1.name} is {person1.age} years old.")

# Using the class method as an alternative constructor
person2 = Person.create_person_from_birth_year("Bob", 1990)
print(f"{person2.name} is {person2.age} years old.")