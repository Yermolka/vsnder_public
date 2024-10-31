from flask import session
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
async def verify_password(username: str | None, password: str | None) -> bool:
    if not username or not password:
        return False
    
    return session.get("username", None) is not None
