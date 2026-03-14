import subprocess
import sys

import django
from django.conf import settings

if not settings.configured:
    settings.configure(
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "wagtail",
            "wagtail.admin",
            "wagtail.documents",
            "wagtail.images",
            "wagtail.search",
            "wagtail.snippets",
            "wagtail.users",
            "wagtail.contrib.settings",
            "wagtail.contrib.forms",
            "wagtail.contrib.redirects",
            "wagtail.contrib.routable_page",
            "wagtail.sites",
            "taggit",
            "rest_framework",
        ],
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        WAGTAIL_SITE_NAME="Test",
        ROOT_URLCONF="django.contrib.admin.sites",
        STATIC_URL="/static/",
    )

django.setup()

sys.exit(
    subprocess.call(
        [
            sys.executable,
            "-m",
            "mypy.stubtest",
            "wagtail",
            "--allowlist",
            "stubtest-allowlist.txt",
            "--mypy-config-file",
            "stubtest_mypy.ini",
        ]
    )
)
