from typing import TypedDict

class Person(TypedDict):
  name: str
  age: int
  email: str 

person = Person(name="John Doe", age=30, email="john@mailinator.com")
person = Person(name="John Doe", age='30', email="john@mailinator.com")
print(person)