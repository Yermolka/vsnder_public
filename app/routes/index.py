from flask import request, render_template
from queries.get_user_by_username import get_user_by_username
from commands.update_user_by_username import update_user_by_username
from utils.auth import auth


@auth.login_required
async def get_index():
    user = await get_user_by_username(auth.username())
    
    return render_template("index.html", user_info=user)


@auth.login_required
async def post_index():
        data = {
            "age": request.form["age"],
            "orientation": request.form["orientation"],
            "interests": request.form["interests"],
            "vsn_interests": request.form["vsn_interests"],
            "places_to_visit": request.form["places_to_visit"],
            "study_places": request.form["study_places"],
            "music": request.form["music"],
            "favorite_movies": request.form["favorite_movies"],
            "religion": request.form["religion"],
            "status": request.form["status"],
            "future_plans": request.form["future_plans"],
            "family_opinion": request.form["family_opinion"],
            "favorite_programming_language": request.form[
                "favorite_programming_language"
            ],
            "lizards_or_russians": request.form.get("lizards_or_russians") == "on",
            "smoking": request.form["smoking"],
            "top_3_people": request.form["top_3_people"],
            "drinking": request.form["drinking"],
        }

        await update_user_by_username(auth.username(), data)
        user = await get_user_by_username(auth.username())

        return render_template("index.html", user_info=user)
