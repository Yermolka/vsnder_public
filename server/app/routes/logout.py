from flask import session, redirect, url_for
from utils.auth import auth

@auth.login_required
async def post_logout():
    session.clear()

    return redirect(url_for("login"))
