import os
from django.core.management.utils import get_random_secret_key

SECRET_KEY = os.getenv("SECRET_KEY", get_random_secret_key())
DEBUG = False

#ALLOWED_HOSTS: list[str] = ['*']
ALLOWED_HOSTS: [
	"195.200.1.214",
	"comunadaterra.com.br",
	"195.200.1.214/api",
	"comunadaterra.com.br/api",
	"195.200.1.214/api/",
	"comunadaterra.com.br/api/",
]

DATABASES = {
    "default": {
        # "ENGINE": "django.db.backends.sqlite3",
        # "NAME": BASE_DIR / "db.sqlite3",
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": "195.200.1.214",
        "PORT": 5432,
    }
}
