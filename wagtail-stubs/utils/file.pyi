from typing import IO

HASH_READ_SIZE: int

def hash_filelike(filelike: IO[bytes]) -> str: ...
