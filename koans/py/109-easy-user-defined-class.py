"""
Koan to learn annotating the class
"""
import datetime
import random
from string import ascii_letters
from typing import TypedDict


# Annotate the user data to fit the get_random_user_data
class UserData(TypedDict):
    name: str
    email: str
    is_active: bool
    last_seen: datetime.date


def get_random_user_data() -> UserData:
    generated_string: str = "".join(random.choice(ascii_letters) for x in range(15))
    return {
        "name": generated_string,
        "email": f"{generated_string}@gmail.com",
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


class User:
    # Annotate the method arguments
    def __init__(
        self, name: str, email: str, is_active: bool, last_seen: datetime.date
    ):
        self.name = name
        self.email = email
        self.is_active = is_active
        self.last_seen = last_seen


# Annotate input arguments and return type as User
def create_user(
    name: str, email: str, is_active: bool, last_seen: datetime.date
) -> User:
    return User(name=name, email=email, is_active=is_active, last_seen=last_seen)


def main():
    # Annotate list of users
    users: list[User] = []
    for _ in range(10):
        user_data = get_random_user_data()
        user = create_user(**user_data)
        users.append(user)
    print(users)


if __name__ == "__main__":
    main()
