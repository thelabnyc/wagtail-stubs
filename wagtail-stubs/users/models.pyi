from _typeshed import Incomplete
from django.db import models
from wagtail.admin.localization import get_available_admin_languages as get_available_admin_languages

def upload_avatar_to(instance, filename): ...

class UserProfile(models.Model):
    user: Incomplete
    submitted_notifications: Incomplete
    approved_notifications: Incomplete
    rejected_notifications: Incomplete
    updated_comments_notifications: Incomplete
    preferred_language: Incomplete
    current_time_zone: Incomplete
    avatar: Incomplete
    dismissibles: Incomplete
    class AdminColorThemes(models.TextChoices):
        SYSTEM = ...
        LIGHT = ...
        DARK = ...
    theme: Incomplete
    class AdminContrastThemes(models.TextChoices):
        SYSTEM = ...
        MORE_CONTRAST = ...
    contrast: Incomplete
    class AdminDensityThemes(models.TextChoices):
        DEFAULT = ...
        SNUG = ...
    density: Incomplete
    keyboard_shortcuts: Incomplete
    @classmethod
    def get_for_user(cls, user): ...
    def get_preferred_language(self): ...
    def get_current_time_zone(self): ...
    class Meta:
        verbose_name: Incomplete
        verbose_name_plural: Incomplete
