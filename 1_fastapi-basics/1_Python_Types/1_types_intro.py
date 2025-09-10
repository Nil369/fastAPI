def get_full_name(f_name:str,l_name:str):
    fullName = f_name.capitalize() + " " + l_name.title()
    return fullName

print(get_full_name("Akash","Halder"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age

print(get_name_with_age("Akash Halder",19))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


# As the list is a type that contains some internal types, we put them in square brackets
def process_items(items:list[str]): # Generic Types / Generics
    for item in items:
        print(item)

# Would do the same to declare tuples and sets:
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

# & offcourse for dictionary also:
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
