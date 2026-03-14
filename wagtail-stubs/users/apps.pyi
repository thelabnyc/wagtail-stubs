from django.apps import AppConfig

class WagtailUsersAppConfig(AppConfig):
    name: str
    label: str
    verbose_name: str
    default_auto_field: str
    group_viewset: str
    user_viewset: str
