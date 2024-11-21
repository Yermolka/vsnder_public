from models.user import User
from common.utils.auth import check_password_match
from modules.user.core.queries.get_user_by_username import get_user_by_username


async def auth_by_password(username: str, password: str) -> User:
    user = await get_user_by_username(username)

    if not check_password_match(password, user.password_hash):
        raise Exception("Incorrect password")
    
    return user
