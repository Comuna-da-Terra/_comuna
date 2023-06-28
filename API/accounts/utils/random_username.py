from accounts.models import User
import random
import string

def random_username(size=8, chars=string.ascii_uppercase + string.digits):
    
    username = ''.join(random.choice(chars) for _ in range(size))
    
    if User.objects.filter(username=username).exists():
        return random_username(size, chars)
    
    else:
        return username
