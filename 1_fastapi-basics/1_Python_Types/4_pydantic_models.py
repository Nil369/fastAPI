from datetime import datetime
from pydantic import BaseModel # Pydantic is a Python library to perform data validation.

# We declare the "shape" of the data as classes with attributes. And each attribute has a type.

# Then we create an instance of that class with some values and
# it will validate the values, convert them to the appropriate type
# (if that's the case) and give you an object with all the data.

class User(BaseModel):
    id:int
    name:str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id":"123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", "3"],
}

user = User(**external_data) # keyword arguments

# same as the above line:
# user = User(id=external_data['id'],
#            signup_ts=external_data['signup_ts'],
#            friends=external_data['friends'])

print(user)
print(user.id)

""" In the above code:
we defined a blueprint for user data with fields like id, name, signup time, and friends.
The class then takes a dictionary with sample user data and creates a User object.
Pydantic checks if the data matches the blueprint, converts it to the correct types,
and then prints the User object and the user's ID.
"""


# METADATA:

# We can use this space in Annotated to provide FastAPI with additional metadata
# about how you want your application to behave.

# The important thing to remember is that the first type parameter you pass to Annotated
# is the actual type. The rest, is just metadata for other tools.

from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

