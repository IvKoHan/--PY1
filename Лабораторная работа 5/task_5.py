from string import ascii_letters, digits
from random import sample


def get_random_password(length: int = 8) -> str:
    if not isinstance(length, int):
        raise TypeError(f"Длина пароля должна быть типом int, а не {type(length)}.")

    return ''.join(sample(ascii_letters + digits, length))


print(get_random_password())
print(get_random_password(15))
