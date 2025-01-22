"""
We can declare that a variable can be any of several types, for example, an int OR a str.

In Python 3.6 and above (including Python 3.10) we can use the Union type
from typing and put inside the square brackets the possible types to accept.

```
from typing import Union

def process_item(item: Union[int, str]):
    print(item)
```

In Python 3.10 there's also a new syntax where we can put
the possible types separated by a vertical bar (|).
"""

# New & Modern Syntax for Union:
def process_items(item: str|int):
    print(item)


# Using Optional[str] instead of just str will let the editor help you detect errors
# where you could be assuming that a value is always a str, when it could actually be None too.
# Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
# This also means that in Python 3.10, you can use Something | None:
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


