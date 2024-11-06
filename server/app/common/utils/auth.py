from hashlib import sha256

from common.consts import PASSWORD_HASH_SALT


def get_password_hash(password: str):
    m = sha256()
    m.update(password.encode("utf-8"))
    m.update(PASSWORD_HASH_SALT)
    return m.hexdigest()


def check_password_match(password: str, password_hash: str):
    return get_password_hash(password) == password_hash
