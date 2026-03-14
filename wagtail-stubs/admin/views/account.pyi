from _typeshed import Incomplete
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from functools import cached_property as cached_property
from wagtail import hooks as hooks
from wagtail.admin import messages as messages
from wagtail.admin.forms.account import AvatarPreferencesForm as AvatarPreferencesForm, LocalePreferencesForm as LocalePreferencesForm, NameEmailForm as NameEmailForm, NotificationPreferencesForm as NotificationPreferencesForm, ThemePreferencesForm as ThemePreferencesForm
from wagtail.admin.forms.auth import LoginForm as LoginForm, PasswordChangeForm as PasswordChangeForm, PasswordResetForm as PasswordResetForm
from wagtail.admin.localization import get_available_admin_languages as get_available_admin_languages, get_available_admin_time_zones as get_available_admin_time_zones
from wagtail.admin.views.generic import EditView as EditView, WagtailAdminTemplateMixin as WagtailAdminTemplateMixin
from wagtail.log_actions import log as log
from wagtail.users.models import UserProfile as UserProfile
from wagtail.utils.loading import get_custom_form as get_custom_form

def get_user_login_form(): ...
def get_password_reset_form(): ...
def password_management_enabled(): ...
def email_management_enabled(): ...
def password_reset_enabled(): ...

class SettingsTab:
    name: Incomplete
    title: Incomplete
    order: Incomplete
    def __init__(self, name, title, order: int = 0) -> None: ...

profile_tab: Incomplete
notifications_tab: Incomplete

class BaseSettingsPanel:
    name: str
    title: str
    tab = profile_tab
    help_text: Incomplete
    template_name: str
    form_class: Incomplete
    form_object: str
    request: Incomplete
    user: Incomplete
    profile: Incomplete
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
    title: Incomplete
    order: int
    template_name: str
    form_class = AvatarPreferencesForm
    form_object: str

class NotificationsSettingsPanel(BaseSettingsPanel):
    name: str
    title: Incomplete
    tab = notifications_tab
    order: int
    form_class = NotificationPreferencesForm
    form_object: str
    def is_active(self): ...

class LocaleSettingsPanel(BaseSettingsPanel):
    name: str
    title: Incomplete
    order: int
    form_class = LocalePreferencesForm
    form_object: str
    def is_active(self): ...

class ThemeSettingsPanel(BaseSettingsPanel):
    name: str
    title: Incomplete
    order: int
    form_class = ThemePreferencesForm
    form_object: str

class ChangePasswordPanel(BaseSettingsPanel):
    name: str
    title: Incomplete
    order: int
    form_class = PasswordChangeForm
    def is_active(self): ...
    def get_form(self): ...

class AccountView(WagtailAdminTemplateMixin, TemplateView):
    template_name: str
    page_title: Incomplete
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
    success_url: Incomplete
    def get_form_class(self): ...

class PasswordResetDoneView(PasswordResetEnabledViewMixin, auth_views.PasswordResetDoneView):
    template_name: str

class PasswordResetConfirmView(PasswordResetEnabledViewMixin, auth_views.PasswordResetConfirmView):
    template_name: str
    success_url: Incomplete

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
    @property
    def next_page(self): ...
    def dispatch(self, request, *args, **kwargs): ...
