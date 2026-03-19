from django.contrib.auth.models import AbstractBaseUser

class MenuItem:
    label: str
    url: str
    icon_name: str
    priority: int
    def __init__(self, label: str, url: str, icon_name: str = "", priority: int = 1000) -> None: ...
    def is_shown(self, user: AbstractBaseUser) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
