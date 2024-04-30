from flask import Flask
from sample import C
from appmap.flask import AppmapFlask


app = Flask(__name__)
AppmapFlask(app).init_app()


@app.route("/")
def hello_world():
    return f"<p>{C().hello_world()}</p>"
