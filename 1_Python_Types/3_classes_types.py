# We can also declare a class as the type of a variable.
# Let's say you have a class Person, with a name:

class Person:
    def __init__(self,name: str):
        self.name = name


def get_person_name(one_person:Person):
    return one_person.name

person_obj = Person("Akash Halder")
print(get_person_name(person_obj))