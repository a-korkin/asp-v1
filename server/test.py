from passlib.hash import bcrypt
from passlib.context import CryptContext

h = bcrypt.hash("password")

print(h)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_pwd_hash(password):
    return pwd_context.hash(password)
