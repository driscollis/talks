from typing import NewType

UserId = NewType('UserId', int)

def get_user_name(user_id: UserId) -> str:
    # ... implementation details ...
    return f"User-{user_id}"

user_b = get_user_name(UserId(123))
