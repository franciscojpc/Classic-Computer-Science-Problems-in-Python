from secrets import token_bytes
from typing import Tuple


def random_key(lenght: int) -> int:
    # Generate lenght random bytes
    tb: bytes = token_bytes(lenght)
    # Convert those bytes into a bit string and return it
    return int.from_bytes(tb, 'big')  

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, 'big')
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


if __name__ == '__main__':
    lenght = 6
    val = random_key(lenght=lenght)
    print(val)