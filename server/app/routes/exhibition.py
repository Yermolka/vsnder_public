from flask import render_template
from queries.get_users import get_users
from utils.auth import auth


@auth.login_required
async def get_exhibition():
    users = await get_users()

    return render_template("exhibition.html", users=users)
