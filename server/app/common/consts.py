from typing import Final


PASSWORD_HASH_SALT: Final[str] = "abobaSvOZOOOooooV".encode("utf-8")

USER_SESSION_COOKIE_NAME: Final[str] = "SESSION_ID"
USER_SESSION_TIMEOUT: Final[int] = 60 * 60
USER_SESSION_USER_ID_KEY: Final[str] = "user_id"
