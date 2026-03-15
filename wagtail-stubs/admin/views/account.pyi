from functools import cached_property as cached_property

from django.contrib.auth import views as auth_views
from django.contrib.auth.models import AbstractBaseUser
from django.http import HttpRequest
from django.views.generic.base import TemplateView
from wagtail import hooks as hooks
from wagtail.admin import messages as messages
from wagtail.admin.forms.account import (
    AvatarPreferencesForm as AvatarPreferencesForm,
)
from wagtail.admin.forms.account import (
    LocalePreferencesForm as LocalePreferencesForm,
)
from wagtail.admin.forms.account import (
    NameEmailForm as NameEmailForm,
)
from wagtail.admin.forms.account import (
    NotificationPreferencesForm as NotificationPreferencesForm,
)
from wagtail.admin.forms.account import (
    ThemePreferencesForm as ThemePreferencesForm,
)
from wagtail.admin.forms.auth import (
    LoginForm as LoginForm,
)
from wagtail.admin.forms.auth import (
    PasswordChangeForm as PasswordChangeForm,
)
from wagtail.admin.forms.auth import (
    PasswordResetForm as PasswordResetForm,
)
from wagtail.admin.localization import (
    get_available_admin_languages as get_available_admin_languages,
)
from wagtail.admin.localization import (
    get_available_admin_time_zones as get_available_admin_time_zones,
)
from wagtail.admin.views.generic import EditView as EditView
from wagtail.admin.views.generic import WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.log_actions import log as log
from wagtail.users.models import UserProfile as UserProfile
from wagtail.utils.loading import get_custom_form as get_custom_form

def get_user_login_form(): ...
def get_password_reset_form(): ...
def password_management_enabled(): ...
def email_management_enabled(): ...
def password_reset_enabled(): ...

class SettingsTab:
    name: str
    title: str
    order: int
    def __init__(self, name, title, order: int = 0) -> None: ...

profile_tab: SettingsTab
notifications_tab: SettingsTab

class BaseSettingsPanel:
    name: str
    title: str
    tab = profile_tab
    help_text: str | None
    template_name: str
    form_class: type | None
    form_object: str
    request: HttpRequest
    user: AbstractBaseUser
    profile: UserProfile
    def __init__(self, request, user, profile) -> None: ...
    def is_active(self): ...
    def get_form(self): ...
    def get_context_data(self): ...
    def render(self): ...

class NameEmailSettingsPanel(BaseSettingsPanel):
    name: str
    order: int
    form_class = NameEmailForm
    @cached_property
    def title(self): ...

class AvatarSettingsPanel(BaseSettingsPanel):
    name: str
    title: str
    order: int
    template_name: str
    form_class = AvatarPreferencesForm
    form_object: str

class NotificationsSettingsPanel(BaseSettingsPanel):
    name: str
    title: str
    tab = notifications_tab
    order: int
    form_class = NotificationPreferencesForm
    form_object: str
    def is_active(self): ...

class LocaleSettingsPanel(BaseSettingsPanel):
    name: str
    title: str
    order: int
    form_class = LocalePreferencesForm
    form_object: str
    def is_active(self): ...

class ThemeSettingsPanel(BaseSettingsPanel):
    name: str
    title: str
    order: int
    form_class = ThemePreferencesForm
    form_object: str

class ChangePasswordPanel(BaseSettingsPanel):
    name: str
    title: str
    order: int
    form_class = PasswordChangeForm
    def is_active(self): ...
    def get_form(self): ...

class AccountView(WagtailAdminTemplateMixin, TemplateView):
    template_name: str
    page_title: str
    header_icon: str
    def get_breadcrumbs_items(self): ...
    def get_context_data(self, **kwargs): ...
    def get_panels(self): ...
    def get_panels_by_tab(self, panels): ...
    def get_menu_items(self): ...
    def get_media(self, panels): ...
    def post(self, request): ...

class PasswordResetEnabledViewMixin:
    def dispatch(self, *args, **kwargs): ...

class PasswordResetView(PasswordResetEnabledViewMixin, auth_views.PasswordResetView):
    template_name: str
    email_template_name: str
    subject_template_name: str
    success_url: str
    def get_form_class(self): ...

class PasswordResetDoneView(PasswordResetEnabledViewMixin, auth_views.PasswordResetDoneView):
    template_name: str

class PasswordResetConfirmView(PasswordResetEnabledViewMixin, auth_views.PasswordResetConfirmView):
    template_name: str
    success_url: str

class PasswordResetCompleteView(PasswordResetEnabledViewMixin, auth_views.PasswordResetCompleteView):
    template_name: str

class LoginView(auth_views.LoginView):
    template_name: str
    def get_success_url(self): ...
    def get(self, *args, **kwargs): ...
    def get_form_class(self): ...
    def form_valid(self, form): ...
    def get_context_data(self, **kwargs): ...

class LogoutView(auth_views.LogoutView):
    next_page: str
    def dispatch(self, request, *args, **kwargs): ...
