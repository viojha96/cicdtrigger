import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    image_tag = os.getenv("APP_IMAGE_TAG", "unknown")
    return f"Hello, world! I'm running an updated app version viojha: {image_tag}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
