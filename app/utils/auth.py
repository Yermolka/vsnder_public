from flask_httpauth import HTTPBasicAuth
from queries.get_user_password_by_username import get_user_password_by_username

auth = HTTPBasicAuth()

@auth.verify_password
async def verify_password(username: str | None, password: str | None) -> bool:
    if not username or not password:
        return False
    
    if (res := await get_user_password_by_username(username, password)):
        return res
    
    return False
