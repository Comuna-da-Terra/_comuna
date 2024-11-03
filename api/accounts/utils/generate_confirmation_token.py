from django.urls import reverse
from itsdangerous import BadSignature, SignatureExpired, URLSafeTimedSerializer
from django.conf import settings

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    return serializer.dumps(email, salt=settings.SECRET_KEY)

def confirm_token(token, expiration=600):
    serializer = URLSafeTimedSerializer(settings.SECRET_KEY)
    try:
        email = serializer.loads(token, salt=settings.SECRET_KEY, max_age=expiration)
    except SignatureExpired:        
        return "O token expirou."
    except BadSignature:
        return "Token inválido."
    return email
