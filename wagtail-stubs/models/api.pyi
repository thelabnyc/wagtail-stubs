from typing import Self
import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

BASE62_ALPHABET: str
BASE62_CHARS: frozenset[str]
TOKEN_PREFIX: str
KEY_SECRET_BYTES: int
KEY_SECRET_LENGTH: int
KEY_CHECKSUM_LENGTH: int
KEY_SALT: str
DISPLAY_PREFIX_LENGTH: int

class APIToken(models.Model):
    id: int
    user: models.ForeignKey[AbstractBaseUser, AbstractBaseUser]
    name: models.CharField[str, str]
    key_hash: models.CharField[str, str]
    prefix: models.CharField[str, str]
    created: models.DateTimeField[datetime.datetime, datetime.datetime]
    revoked_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]
    last_used_at: models.DateTimeField[datetime.datetime | None, datetime.datetime | None]

    class Meta:
        verbose_name: str
        verbose_name_plural: str

    @classmethod
    def generate_token(cls) -> str: ...
    @classmethod
    def validate_token_format(cls, token: str) -> bool: ...
    @classmethod
    def hash_token(cls, token: str, secret_key: str | bytes | None = None) -> str: ...
    @classmethod
    def candidate_key_hashes(cls, token: str) -> list[str]: ...
    @classmethod
    def create_token(cls, *, user: AbstractBaseUser, name: str) -> tuple[Self, str]: ...
    def revoke(self) -> None: ...
