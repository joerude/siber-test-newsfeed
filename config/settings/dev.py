from .base import *

INSTALLED_APPS.extend(
    [
        "debug_toolbar",
    ],
)


INTERNAL_IPS = [
    "127.0.0.1",

]

MIDDLEWARE.extend(
    [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
    ],
)

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG,
    "SHOW_TEMPLATE_CONTEXT": True,
}
