""" test extension """
import flask

import flask_api_json_encoder


def test_extension():
    """test extension"""
    app = flask.Flask(__name__)

    assert flask_api_json_encoder.APIJsonEncoder(app)
    assert isinstance(app.json, flask_api_json_encoder.JSONEncoder)


def test_extension_no_app():
    """test extension without an app"""
    assert flask_api_json_encoder.APIJsonEncoder()
