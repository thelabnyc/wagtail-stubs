import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.mypy_test_settings")

import django

django.setup()

# Run stubtest in-process so Django's app registry (populated above) is
# available when stubtest imports wagtail modules at runtime.
# stubtest.main() reads from sys.argv, so we patch it.
sys.argv = [
    "stubtest",
    "wagtail",
    "--allowlist",
    "stubtest-allowlist.txt",
    "--mypy-config-file",
    "stubtest_mypy.ini",
]

from mypy.stubtest import main  # noqa: E402

sys.exit(main())
