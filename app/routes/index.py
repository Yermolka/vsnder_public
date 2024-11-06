from flask import request, render_template, session
from queries.get_user_by_username import get_user_by_username
from commands.update_user_by_username import update_user_by_username
from utils.auth import auth
from models.user import PutUserDto


@auth.login_required
async def get_index():
    user = await get_user_by_username(session["username"])
    
    return render_template("index.html", user_info=user)


@auth.login_required
async def post_index():
        dto = PutUserDto.from_dict(request.form | {"username": auth.username()})

        await update_user_by_username(dto)
        user = await get_user_by_username(auth.username())

        return render_template("index.html", user_info=user)
