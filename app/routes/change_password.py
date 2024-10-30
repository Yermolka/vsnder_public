from flask import request, render_template, flash, redirect, url_for
from utils.auth import auth
from commands.change_password_by_username import change_password_by_username


@auth.login_required
async def get_change_password():
    return render_template("change_password.html")


@auth.login_required
async def post_change_password():
    old_password = request.form["old_password"]
    new_password = request.form["new_password"]
    confirm_password = request.form["confirm_password"]

    if new_password != confirm_password:
        flash("Passwords do not match!")
        return redirect(url_for("change_password"))

    change_password_by_username(auth.username(), old_password, new_password)

    return redirect(url_for("index"))
