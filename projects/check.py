import bcrypt

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    plain_password = plain_password.encode('utf-8')

    return bcrypt.checkpw(plain_password, hashed_password.encode('utf-8'))

if __name__ == "__main__":
    # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # passwd = b's$cret12'
    # salt = bcrypt.gensalt()
    # hashed = bcrypt.hashpw(passwd, salt)
    #
    # print(salt)
    # print(hashed)
    #
    # if bcrypt.checkpw(passwd, hashed):
    #     print("match")
    # else:
    #     print("does not match")

    hashed = hash_password("pipp")
    print(hashed)

    verify_password("pipp", hashed)