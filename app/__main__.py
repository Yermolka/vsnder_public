from flask import Flask
from flask_session import Session
from cachelib.file import FileSystemCache
import os

from routes import (
    get_index,
    post_index,
    get_change_password,
    post_change_password,
    get_exhibition,
    get_user,
    get_login,
    post_login,
)


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "aboba")
SESSION_TYPE = "cachelib"
SESSION_SERIALIZATION_FORMAT = "json"
SESSION_CACHELIB = FileSystemCache(threshold=500, cache_dir="/sessions")
app.config.from_object(__name__)
Session(app)

if __name__ == "__main__":
    app.add_url_rule("/", endpoint="index", view_func=get_index, methods=["GET"])
    app.add_url_rule("/", view_func=post_index, methods=["POST"])

    app.add_url_rule(
        "/change_password",
        endpoint="change_password",
        view_func=get_change_password,
        methods=["GET"],
    )
    app.add_url_rule(
        "/change_password", view_func=post_change_password, methods=["POST"]
    )

    app.add_url_rule(
        "/exhibition", endpoint="exhibition", view_func=get_exhibition, methods=["GET"]
    )

    app.add_url_rule("/user/<int:id>", endpoint="user", view_func=get_user, methods=["GET"])

    app.add_url_rule("/login", endpoint="login", view_func=get_login, methods=["GET"])
    app.add_url_rule("/login", view_func=post_login, methods=["POST"])

    app.run(host="0.0.0.0", port=8080, debug=True)
