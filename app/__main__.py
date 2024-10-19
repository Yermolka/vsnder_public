from flask import Flask
import os
from routes import get_index, post_index, get_change_password, post_change_password


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "aboba")

if __name__ == "__main__":
    app.add_url_rule("/", endpoint="index", view_func=get_index, methods=["GET"])
    app.add_url_rule("/", view_func=post_index, methods=["POST"])

    app.add_url_rule("/change_password", endpoint="change_password", view_func=get_change_password, methods=["GET"])
    app.add_url_rule("/change_password", view_func=post_change_password, methods=["POST"])

    app.run(host="0.0.0.0", port=8080, debug=True)
