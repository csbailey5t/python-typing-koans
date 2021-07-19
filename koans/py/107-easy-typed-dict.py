"""
Koan to learn annotating the dictionary with fixed key/values.
"""

import datetime
import random
from typing import TypedDict
from uuid import UUID, uuid4


class User(TypedDict):
    user_id: UUID
    company_id: int
    is_active: bool
    last_seen: datetime.date


# Annotate the return type as TypedDict
# Documentation: https://docs.python.org/3/library/typing.html#typing.TypedDict
def get_random_user_data() -> User:
    return {
        "user_id": uuid4(),
        "company_id": random.randint(1, 1_000_000),
        "is_active": random.choice([True, False]),
        "last_seen": datetime.datetime.utcnow(),
    }


print(get_random_user_data())
