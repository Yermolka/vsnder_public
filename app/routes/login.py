from flask import request, render_template, session, redirect, url_for, flash
from queries.get_user_password_by_username import get_user_password_by_username


async def get_login():
    return render_template("login.html")


async def post_login():
    data = request.form

    if get_user_password_by_username(data["username"], data["password"]):
        session["username"] = data["username"]
        return redirect(url_for("exhibition"))

    flash("Invalid username or password")
