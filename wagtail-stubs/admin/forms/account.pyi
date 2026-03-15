from typing import Any

from django import forms
from django.contrib.auth.models import AbstractBaseUser
from wagtail.users.models import UserProfile

User: type[AbstractBaseUser]

class NotificationPreferencesForm(forms.ModelForm[UserProfile]):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Meta:
        model: type[UserProfile]
        fields: list[str]
        widgets: dict[str, forms.Widget]

class LocalePreferencesForm(forms.ModelForm[UserProfile]):
    preferred_language: forms.ChoiceField
    current_time_zone: forms.ChoiceField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Meta:
        model: type[UserProfile]
        fields: list[str]

class NameEmailForm(forms.ModelForm[AbstractBaseUser]):
    first_name: forms.CharField
    last_name: forms.CharField
    email: forms.EmailField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    class Meta:
        model: type[AbstractBaseUser]
        fields: list[str]

class AvatarPreferencesForm(forms.ModelForm[UserProfile]):
    avatar: forms.ImageField
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save(self, commit: bool = True) -> UserProfile: ...

    class Meta:
        model: type[UserProfile]
        fields: list[str]

class ThemePreferencesForm(forms.ModelForm[UserProfile]):
    class Meta:
        model: type[UserProfile]
        fields: list[str]
