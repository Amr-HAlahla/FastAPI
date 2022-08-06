from passlib.context import CryptContext

# from . import schemas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def bcrypt(password: str):
        hashed_pass = pwd_context.hash(password)
        return hashed_pass

    @staticmethod
    def verify(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
