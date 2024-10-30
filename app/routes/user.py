from flask import render_template
from queries.get_user_by_id import get_user_by_id
from utils.auth import auth


@auth.login_required
async def get_user(id: int):
    user = await get_user_by_id(id)
    
    return render_template("user.html", user=user)
