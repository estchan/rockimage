from flask import Flask, jsonify

from rockimage import config

app = Flask(__name__)


@app.route("/")
def root():
    return jsonify({"message": "Hello Cloud"}), 200


if config.ENABLE_API:
    from rockimage import service

    @app.route("/images")
    def list_images():
        images = service.list_images()
        return jsonify(images), 200

    @app.route("/images/<uuid:str>")
    def get_image(uuid: str):
        image = service.get_image(uuid)
        return jsonify(image), 200
