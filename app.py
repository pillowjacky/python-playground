from flask import Flask
from cat.routes import bp

app = Flask(__name__)
app.register_blueprint(bp)


@app.route("/")
def index():
    return "Hello, World!"
