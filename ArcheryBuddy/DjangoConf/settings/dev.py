from . import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-sm)@ym0y#qr#8pj%liy3va5+3=1ral+v(gkjvf!_^@*b@2m=-6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# django debug toolbar
def show_toolbar(request):
    return True


INSTALLED_APPS += ["debug_toolbar", "django_browser_reload"]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}
INTERNAL_IPS = [
    "127.0.0.1",
]
