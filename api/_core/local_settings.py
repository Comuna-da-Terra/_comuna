SECRET_KEY = '|ev4-IEXh`=YC$d4~yCas}}h2|W}k9%DRs%6czJa#!kQr6Z0#Lq087:xC4&{oE+L'
DEBUG = False

ALLOWED_HOSTS: ['api.comunadaterra.com.br']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'db_comuna',
        'USER': '_comuna',
        'PASSWORD': 'n54xFUB0zZ',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
